from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MWmg8DKKUgEtkfSxPNrUSY2eMxdvII9yzSdL3bwBBF8XL4Xrri4eJ3jhpH35fxoRAd5vRp31R5SSdF7Bq9P4KMV00OiWmEPBm',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
