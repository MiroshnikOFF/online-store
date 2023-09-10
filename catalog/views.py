from django.shortcuts import render

from catalog.models import Product


def home(request):
    # last_products = Product.objects.order_by('-creation_date')[:5]
    # for product in last_products:
    #     print(product)
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Пользователь: {name}\n"
              f"Телефон: {phone}\n"
              f"Сообщение: {message}")
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    context = {
        'object_list': Product.objects.filter(id=pk)
    }
    return render(request, 'catalog/product.html', context)
