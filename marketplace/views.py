from django.shortcuts import render, get_object_or_404
from store.models import Product
from cart.models import CartItem
from .models import Categories
from django.shortcuts import redirect


from cart.models import Cart
from cart.models import CartItem


from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from cart.models import Cart, CartItem
from .models import Categories

def market_place(request):
    categories = Categories.objects.all()
    products = Product.objects.all()[:6]

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart = None
        cart_id = request.session.get('cart_id')
        if cart_id:
            try:
                cart = Cart.objects.get(id=cart_id)
            except Cart.DoesNotExist:
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    cart_items = CartItem.objects.filter(cart=cart, is_active=True) if cart else []

    context = {
        'products': products,
        'categories': categories,
        'total_items': cart_items.count() if cart_items else 0,
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

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart = None
        cart_id = request.session.get('cart_id')
        if cart_id:
            try:
                cart = Cart.objects.get(id=cart_id)
            except Cart.DoesNotExist:
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    cart_items = CartItem.objects.filter(cart=cart, is_active=True) if cart else []

    context = {
        'products' : products,
        'product_count' : product_count,
        'category' : category,
        'selcted_slug' : category_slug,
        'cart_cost': cart_cost,
        'cart_items': cart_items,
        'total_items': cart_items.count() if cart_items else 0,
    }

    return render(request, 'temp_marketplace/categoryProductList.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart = None
        cart_id = request.session.get('cart_id')
        if cart_id:
            try:
                cart = Cart.objects.get(id=cart_id)
            except Cart.DoesNotExist:
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    cart_items = CartItem.objects.filter(cart=cart, is_active=True) if cart else []
    context = {
        'single_product' : single_product,
        'total_items': cart_items.count() if cart_items else 0,

    }
    return render(request, "temp_marketplace/product_details.html",context)


def allProducts(request):
    products = Product.objects.filter(is_available=True)
    product_count = products.count()

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart = None
        cart_id = request.session.get('cart_id')
        if cart_id:
            try:
                cart = Cart.objects.get(id=cart_id)
            except Cart.DoesNotExist:
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    cart_items = CartItem.objects.filter(cart=cart, is_active=True) if cart else []
    context = {
        'products': products,
        'product_count': product_count,
        'total_items': cart_items.count() if cart_items else 0,
    }

    return render(request, 'temp_marketplace/allProducts.html', context)