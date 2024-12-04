from django.shortcuts import render, redirect
from .forms import ProductForm


def product_list(request):
    form = ProductForm()  # Создаем экземпляр формы

    return render(request, 'create_product.html', {'form': form})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Сохранить новый продукт
            return redirect('/')  # Переадресовать на список продуктов (или на другую страницу)
    else:

        return redirect('/')
