from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    category_list = Product.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Товары'
    }
    return render(request, "catalog/home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")

    context = {
        'title': 'Контакты'
    }
    return render(request, "catalog/contacts.html")


def product(request, pk):
    product_card = Product.objects.get(pk=pk)
    context = {
        'object': product_card
    }
    return render(request, 'catalog/product.html', context)
