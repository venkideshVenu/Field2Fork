from django.shortcuts import render
from marketplace.models import Product
from marketplace.models import Categories
# Create your views here.
from cart.models import CartItem
from .models import Categories


def market_place(request):
    categories = Categories.objects.all()
    product = Product.objects.all().filter(is_available=True)
    product = product[:8]
    context = {
        'total_items': len(CartItem.objects.all()),
        'products':product,
        'categories': categories,
        }
    return render(request, 'temp_marketplace/mainpage.html', context)

def store(request, category_slug=None,cart_cost=0,cart_items=0):
    category = None
    products = None
    cart_cost = 2000
    cart_items = 5

    if category_slug != None:
        category = get_object_or_404(Categories, slug=category_slug )
        products = Product.objects.filter(category=category , is_available= True) 
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available= True)
        product_count = products.count()

    context = {
        'products' : products,
        'product_count' : product_count,
        'category' : category,
        'selcted_slug' : category_slug,
        'cart_cost': cart_cost,
        'cart_items': cart_items,
        'total_items': len(CartItem.objects.all()),
    }

    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product' : single_product,
        'total_items': len(CartItem.objects.all()),

    }

    return render(request, "store/product_detail.html",context)