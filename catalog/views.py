from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self):
        context_data = super().get_context_data()
        context_data['object_list'] = Product.objects.all()
        return context_data


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Пользователь: {name}\n"
              f"Телефон: {phone}\n"
              f"Сообщение: {message}")
    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        current_versions = Version.objects.filter(is_current_version=True)
        context_data['current_versions'] = current_versions
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')


def get_versions_by_product(request, **kwargs):
    product_pk = kwargs.get('pk')
    queryset = Version.objects.filter(product=product_pk)
    context = {'queryset': queryset, 'product_pk': product_pk}
    return render(request, 'catalog/product_versions.html', context)


def show_version(request, **kwargs):
    version_pk = kwargs.get('version_pk')
    version = Version.objects.get(pk=version_pk)
    product_pk = version.product.pk
    context = {'version': version, 'product_pk': product_pk}
    return render(request, 'catalog/product_version_detail.html', context)










