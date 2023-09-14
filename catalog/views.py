from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from catalog.models import Product


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

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset
