from django.forms import ModelForm
from .models import BurdenSheet, ProductOrder

class BurdenSheetForm(ModelForm):
	class Meta:
		model = BurdenSheet
		fields = ['customer', 'description', 'total_amount','date']


class ProductOrderForm(ModelForm):
	class Meta:
		model = ProductOrder
		fields = ['name', 'amount','price', 'discount']
