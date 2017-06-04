# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import logging
logger = logging.getLogger("django.server")
from django.contrib import admin

# Register your models here.
from .models import BurdenSheet, ProductOrder, ProductName, Customer, CustomerProduct


class ProductOrderInline(admin.TabularInline):
    verbose_name = "公司备料"
    model = ProductOrder
    #readonly_fields = ('account_payable',)
    extra = 3
    exclude = ('date',)


class CustomerProductInline(admin.TabularInline):
    verbose_name = "客户来料"
    model = CustomerProduct
    extra = 3
    exclude = ('date',)


class BurdenSheetAdmin(admin.ModelAdmin):
    inlines = [
        ProductOrderInline,
        CustomerProductInline,
    ]
    #readonly_fields = ('total_amount', 'total_payable', 'total_discount',)
    exclude = ('time_stamp',)

    class Media:
        js = ("js/auto_fill.js",)

    def update_burden_sheet(self, obj):
        product_orders = ProductOrder.objects.filter(burden_sheet=obj)
        customer_products = CustomerProduct.objects.filter(burden_sheet=obj)
        total_discount = 0
        total_payable = 0
        total_amount = 0
        for product_order in product_orders:
            total_discount += product_order.discount
            total_payable += product_order.account_payable
            total_amount += product_order.amount

        for customer_product in customer_products:
            total_amount += customer_product.amount
        obj.total_discount = total_discount
        obj.total_amount = total_amount
        obj.total_payable = total_payable
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        obj = form.instance
        for instance in instances:
            instance.date = obj.date
            instance.save()
        formset.save_m2m()
        if formset.deleted_objects:
            self.update_burden_sheet(obj)


admin.site.register(BurdenSheet, BurdenSheetAdmin)
admin.site.register(ProductName)
admin.site.register(Customer)