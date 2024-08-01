from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart
from cart.models import CartItem

from store.models import Product
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def _cart_id(request):
    if request.user.is_authenticated:
        return str(request.user.id)
    else:
        cart = request.session.session_key
        if not cart:
            cart = request.session.create()
        return cart

def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart_id = _cart_id(request)
        cart, created = Cart.objects.get_or_create(cart_id=cart_id)
    return cart

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = get_or_create_cart(request)

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )

    # Get the URL of the page that made the request
    next_page = request.META.get('HTTP_REFERER')
    
    if next_page:
        # If there's a valid referring page, redirect back to it
        return HttpResponseRedirect(next_page)
    else:
        # If there's no valid referring page, redirect to a default page (e.g., marketplace)
        return HttpResponseRedirect(reverse('marketpage'))

def remove_cart(request, product_id):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def delete_cart(request, product_id):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')



def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = get_or_create_cart(request)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    except:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'total_items': cart_items.count() if cart_items else 0,
    }
    
    return render(request, "temp_marketplace/cart.html", context)
