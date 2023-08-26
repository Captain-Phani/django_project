from django.contrib import admin
from .models import Product,Discount,CheckOut,Cart
# Register your models here.
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(CheckOut)
admin.site.register(Cart)
