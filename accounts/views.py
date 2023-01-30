from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, Page
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.

def dashBoard(request):
    orders = Order.objects.all().order_by("-date_created")
    customers = Customer.objects.all().order_by("-date_created")

    customers_list = Paginator(customers, 5)
    orders_list = Paginator(orders, 5)

    context = {
        "orders_delivered": orders.filter(status="Delivered"),
        "orders_pending":orders.filter(status="Pending"),
        "orders":orders,
        "customers":customers,
        "customers_list":customers_list,
        "orders_list":orders_list,
    }
    return render(request, "accounts/dashboard.html", context)

def products(request):
    products_all = Product.objects.all().order_by("name")
    context = {
        "products_all":products_all
    }
    return render(request, "accounts/products.html", context)

def customerPage(request, customer_id):
    needed_customer = get_object_or_404(Customer, id = customer_id)
    orders = needed_customer.order_set.all().order_by("-date_created")
    return render(request, "accounts/customer.html", {"needed_customer":needed_customer, "orders":orders})

# def customerPage(request, pk):
#     specificCustomer =
#     return render(request, "accounts/specific_customer.html", {"get_customer":specificCustomer, "title": f"Customer|{specificCustomer.name}"})

class CreateCustomerView(CreateView):
    model = Customer
    fields = ["name", "phone", "email"]
    template_name = "accounts/create_customer.html"


class UpdateCustomerView(UpdateView):
    model = Customer
    template_name = "accounts/update_customer.html"

class DeleteCustomerView(DeleteView):
    model = Customer
    template_name = "accounts/delete_confirmation.html"

    success_url = "/accounts/"