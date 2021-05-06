from django.shortcuts import get_object_or_404, render

#get_object_or_404 is a short cut way of accessing the data from Db
from .models import Category, Product

# Create your views here.



def products_all(request):
    products = Product.products.all()
    #{'products':products}(context)-A dictionary of values to add to the template context
    #render(request, template_name, context=None, content_type=None, status=None, using=None)
    #request - object used to generate this response
    #content_type-'text/html'
    return  render(request,'store/home.html',{'products':products})

def product_detail(request,slug):
    book = get_object_or_404(Product, slug=slug, in_stock = True)
    return render(request, 'store/products/single.html', {'products':book})

def category_detail(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category':category,'products': products})


