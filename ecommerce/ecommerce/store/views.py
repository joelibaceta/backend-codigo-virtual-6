
from store.models import Cart, CartItem, Product
from django.shortcuts import render
from django.views.generic import ListView
from store.lib.mercadopago import MercadoPago
from store.lib.culqi import Culqi

ACCESS_TOKEN = "TEST-280207732140858-061501-6206033fcf93d40ef7becedbba955f97-112585375"
mp = MercadoPago(access_token=ACCESS_TOKEN)

SECRET_KEY = "sk_test_gEoUP2liniTAqEws"
culqi = Culqi(secret=SECRET_KEY)

def dopay(request):
    form_data = request.POST
    payment_data = {
        "transaction_amount": 100.0,
        "token": form_data.get("token"), 
        "installments": int(form_data.get("installments")),
        "payment_method_id": form_data.get("payment_method_id"),
        "payer": {
            "email": form_data.get("email"),
            "identification": {
                "type": form_data.get("type"), 
                "number": form_data.get("number")
            }
        }
    }
    payment = mp.create_payment(data=payment_data)
    print(payment)
    if payment["status"] == "approved":

        return render(request, "store/success.html")
    else:
        return render(request, "store/failed.html")


def pay(request):
    return render(request, "store/payment_form.html")

def culqi_pay(request):
    return render(request, "store/culqi_pay.html")

def doculqipay(request):
    form_data = request.POST
    charge_data = {
        "amount": 100,
        "currency_code": "PEN",
        "email": "mail@demo.com",
        "source_id": form_data.get("token"), 
    }
    response = culqi.create_charge(data = charge_data)
    print(response)
    return render(request, "store/success.html")

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
