# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import uuid
import logging
logger = logging.getLogger("django.server")


from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class Customer(models.Model):
    name = models.CharField("姓名", max_length=200, primary_key=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible  # only if you need to support Python 2
class ProductName(models.Model):
    name = models.CharField("名称", max_length=200, primary_key=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible  # only if you need to support Python 2
class BurdenSheet(models.Model):

    initial_date = None

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, verbose_name="客户", max_length=200, blank=False)

    description = models.CharField("摘要", max_length=200, blank=False)
    total_amount = models.FloatField("投料总量", blank=False)
    total_payable = models.FloatField("应付合计", blank=False)
    total_discount = models.FloatField("折扣合计", blank=False, default=0)
    date = models.DateField("生产日期", blank=False)
    time_stamp = models.DateTimeField("time stamp", auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super(BurdenSheet, self).__init__(*args, **kwargs)
        self.initial_date = self.date

    def date_changed(self):
        if self.initial_date != self.date:
            return True
        return False

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.date_changed():
            # date changed - do something here
            product_orders = ProductOrder.objects.filter(burden_sheet=self)
            customer_products = CustomerProduct.objects.filter(burden_sheet=self)
            for product_order in product_orders:
                product_order.date = self.date
                product_order.save()
            for customer_product in customer_products:
                customer_product.date = self.date
                customer_product.save()

        super(BurdenSheet, self).save(force_insert, force_update, *args, **kwargs)
        self.initial_date = self.date

    def __str__(self):
        return self.description


@python_2_unicode_compatible  # only if you need to support Python 2
class ProductOrder(models.Model):
    name = models.ForeignKey(ProductName, verbose_name="名称", null=True, on_delete=models.SET_NULL, blank=False)
    burden_sheet = models.ForeignKey(BurdenSheet, on_delete=models.CASCADE, blank=False)
    amount = models.FloatField("重量", blank=False)
    price = models.FloatField("单价", blank=False)
    discount = models.FloatField("优惠", blank=False)
    account_payable = models.FloatField("应付款", blank=False)
    date = models.DateField("生产日期", blank=False, default=datetime.date.today)

    def __str__(self):
        return self.name.name

@python_2_unicode_compatible  # only if you need to support Python 2
class CustomerProduct(models.Model):
    name = models.ForeignKey(ProductName, verbose_name="名称", null=True, on_delete=models.SET_NULL, blank=False)
    burden_sheet = models.ForeignKey(BurdenSheet, on_delete=models.CASCADE, blank=False)
    amount = models.FloatField("重量", blank=False)
    date = models.DateField("生产日期", blank=False, default=datetime.date.today)

    def __str__(self):
        return self.name.name



