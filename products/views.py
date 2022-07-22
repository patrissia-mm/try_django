from django.http import Http404
from django.shortcuts import render
from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.

def product_list_view(request):
    queryset=Product.objects.all()
    context={
        "object_list":queryset
    }
    return render(request, "products/product_list.html", context)

def dynamic_lookup_view(request, id):
    try:
        obj=Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context={
        "object":obj
    }
    return render(request, 'products/product_detail.html', context)


def render_initial_data(request):
    #initial_data={
    #    'tittle':"Un título al cargar la página"
    #}
    obj=Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj) #initial=initial_data
    if form.is_valid():
        form.save()
        form=ProductForm()
    context={
        "form":form
    }
    return render(request,'products/product_create.html',context)

#Vista para guardar/crear un producto
#def product_create_view(request):
#    my_form=RawProductForm()
#    if request.method=='POST':
#        my_form=RawProductForm(request.POST)
#        if my_form.is_valid():
#            print(my_form.cleaned_data)
#            Product.objects.create(**my_form.cleaned_data)
#        else:
#            print(my_form.errors)
#    context={
#        'form':my_form
#    }
#    return render(request, 'products/product_create.html', context)

#def product_create_view(request):
#    if request.method=="POST":
#        my_new_title=request.POST.get('title')
#        print(my_new_title)
#    context={}
#    return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProductForm()
    context={
        "form":form
    }
    return render(request, "products/product_create.html", context)


#Vista para ver el detalle del producto con id=1
def product_detail_view(request):
    obj=Product.objects.get(id=1)
    context={
        "object":obj
    }
    return render(request, "products/product_detail.html", context)
