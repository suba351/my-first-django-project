from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Product
from .forms import ProductForm, RawProductForm


def render_initial_date(request):
    initial_data = {
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=1)
    form = RawProductForm(request.POST or None, initial=initial_data)
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        # confirming method delete
        obj.delete()
        print(redirect('http://127.0.0.1:8000/admin/'))
        return redirect('http://127.0.0.1:8000/admin/')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context ={
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
