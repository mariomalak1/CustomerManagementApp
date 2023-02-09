from django.forms import ModelForm
from .models import Order, Product, Customer

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'status']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ["date_created"]


