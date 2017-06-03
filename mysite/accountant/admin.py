# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import BurdenSheet, ProductOrder, ProductName, Customer, CustomerProduct


class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    #readonly_fields = ('account_payable',)
    extra = 5

class CustomerProductInline(admin.TabularInline):
    model = CustomerProduct
    extra = 5


class BurdenSheetAdmin(admin.ModelAdmin):
    inlines = [
        ProductOrderInline,
        CustomerProductInline,
    ]
    #readonly_fields = ('total_amount', 'total_payable', 'total_discount',)
    exclude = ('time_stamp',)

    class Media:
        js = ("js/auto_fill.js",)

admin.site.register(BurdenSheet, BurdenSheetAdmin)
admin.site.register(ProductName)
admin.site.register(Customer)