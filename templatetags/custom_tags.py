from django import template
from Groceryapp.models import *
register = template.Library()

@register.filter()
def applydiscount(pid):
    data = Product.objects.get(id=pid)
    price = float(data.price) * (100 - int(data.discount))/100
    return price

@register.simple_tag
def producttotalprice(data, qty):
    product = Product.objects.get(id=data)
    price = float(product.price) * (100 - float(product.discount)) / 100
    return int(qty) * price


@register.filter()
def productname(pid):
    data = Product.objects.get(id=pid)
    return data.name

@register.filter()
def productprice(pid):
    data = Product.objects.get(id=pid)
    return data.price
