from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category
from catalog.services import get_categories_cache


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self):
        context_data = super().get_context_data()
        context_data['object_list'] = Product.objects.all()
        return context_data


@login_required
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Пользователь: {name}\n"
              f"Телефон: {phone}\n"
              f"Сообщение: {message}")
    return render(request, 'catalog/contacts.html')


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        current_versions = Version.objects.filter(is_current_version=True)
        context_data['current_versions'] = current_versions
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        self.object = form.save()
        self.object.autor = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    
    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')


@login_required
@permission_required('catalog.set_is_published_product')
def publish_product(request, pk):
    """Публикует/снимает с публикации продукт"""

    product = Product.objects.get(pk=pk)
    if product.is_published:
        product.is_published = False
    else:
        product.is_published = True
    product.save()
    return redirect('catalog:products')


@login_required
def get_versions_by_product(request, **kwargs):
    product_pk = kwargs.get('pk')
    queryset = Version.objects.filter(product=product_pk)
    context = {'queryset': queryset, 'product_pk': product_pk}
    return render(request, 'catalog/product_versions.html', context)


@login_required
def show_version(request, **kwargs):
    version_pk = kwargs.get('version_pk')
    version = Version.objects.get(pk=version_pk)
    product_pk = version.product.pk
    context = {'version': version, 'product_pk': product_pk}
    return render(request, 'catalog/product_version_detail.html', context)


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = get_categories_cache()
        return queryset








