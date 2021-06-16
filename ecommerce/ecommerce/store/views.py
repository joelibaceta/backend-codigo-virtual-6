
from store.models import Cart, CartItem, Product
from django.shortcuts import render
from django.views.generic import ListView
from store.lib.mercadopago import MercadoPago

ACCESS_TOKEN = "TEST-280207732140858-061501-6206033fcf93d40ef7becedbba955f97-112585375"
mp = MercadoPago(access_token=ACCESS_TOKEN)


def pay(request):
    return render(request, "store/payment_form.html")

def listproduct(request):
    products = Product.objects.all()

    for product in products:
        preference_data = {
            "items": [{
                "title": product.name, 
                "description": "", 
                "unit_price": product.price,
                "currency_id": "PEN",
                "quantity": 1
            }]
        }
        preference = mp.create_preference(data=preference_data)
        print(preference)
        product.init_point = preference["sandbox_init_point"]

    return render(request, 'store/product_list.html', {
        'object_list': products
    })


def buy(request, pk):
    cart_count = Cart.objects.all().count()

    if cart_count > 0:
        cart = Cart.objects.first()
    else:
        cart = Cart()
        cart.save()

    product = Product.objects.get(pk=pk)
    
    item = CartItem()
    item.cart = cart
    item.product = product
    item.save()

    items = CartItem.objects.filter(cart_id=cart.id)

    return render(request, 'store/cart.html', {"items": items} )
