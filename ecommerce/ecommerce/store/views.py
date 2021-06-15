
from store.models import Cart, CartItem, Product
from django.shortcuts import render
from django.views.generic import ListView
from store.lib.mercadopago import MercadoPago

def listproduct(request):
    ACCESS_TOKEN = "TEST-280207732140858-061501-6206033fcf93d40ef7becedbba955f97-112585375"

    mp = MercadoPago(access_token=ACCESS_TOKEN)
    products = Product.objects.all()

    preferences = {}

    for product in products:
        data = {
            "items": [{
                "title": product.name, 
                "unit_price": product.price,
                "currency_id": "PEN",
                "quantity": 1
            }]
        }
        preference = mp.create_preference(data)
        preferences[str(product.id)] = preference["sandbox_init_point"]

    render(request, 'store/product_list', {
        "object_list": products,
        "preferences": preferences
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
