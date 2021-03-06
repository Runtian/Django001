# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import logging
logger = logging.getLogger("django.server")
from django.contrib import admin

# Register your models here.
from .models import (BurdenSheet, ProductOrder, ProductName, Source,
                     CustomerProduct, ProductPurchase, ProcessingFee,
                     Payer, Income, Payee, Expense, CustomerProductName,
                     Account)


class ProductOrderInline(admin.TabularInline):
    verbose_name = "公司备料"
    model = ProductOrder
    #readonly_fields = ('account_payable',)
    extra = 3
    exclude = ('date',)


class ProcessingFeeInline(admin.TabularInline):
    verbose_name = "加工费"
    model = ProcessingFee
    extra = 3
    exclude = ('date',)


class CustomerProductInline(admin.TabularInline):
    verbose_name = "客户来料"
    model = CustomerProduct
    extra = 3
    exclude = ('date',)


class BurdenSheetAdmin(admin.ModelAdmin):
    list_display = ('date', 'customer', 'description', 'total_payable')
    inlines = [
        ProductOrderInline,
        ProcessingFeeInline,
        CustomerProductInline,
    ]
    #readonly_fields = ('total_amount', 'total_payable', 'total_discount',)
    exclude = ('time_stamp',)

    class Media:
        js = ("js/auto_fill?1.js",)

    def update_burden_sheet(self, obj):
        product_orders = ProductOrder.objects.filter(burden_sheet=obj)
        customer_products = CustomerProduct.objects.filter(burden_sheet=obj)
        processing_fees = ProcessingFee.objects.filter(burden_sheet=obj)
        total_payable = 0
        total_amount = 0
        for product_order in product_orders:
            total_payable += product_order.account_payable
            total_amount += product_order.amount
        for processing_fee in processing_fees:
            total_payable += processing_fee.account_payable
        for customer_product in customer_products:
            total_amount += customer_product.amount
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

class ProductPurchaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'source', 'name', 'account_payable')
    class Media:
        js = ("js/product_purchase_auto_fill.js",)


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'payer', 'account', 'description', 'amount')


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'Payee', 'account', 'description', 'amount')

admin.site.register(BurdenSheet, BurdenSheetAdmin)
admin.site.register(ProductPurchase, ProductPurchaseAdmin)

admin.site.register(CustomerProductName)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)

admin.site.register(Source)
admin.site.register(ProductName)
admin.site.register(Payer)
admin.site.register(Payee)
admin.site.register(Account)



