from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, Page
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import OrderForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import is_allowed
from django.utils.decorators import method_decorator
from .forms import ProductForm, CustomerForm
from django.utils import timezone
# Create your views here.
########################
## main page

@login_required
@is_allowed(["admins"])
def dashBoard(request):
    orders = Order.objects.all().order_by("-date_created")
    customers = Customer.objects.all().order_by("-date_created")

    customers_list = []
    orders_list = []
    # Paginator(customers, 5)
    count = 0
    for order_ in orders:
        count += 1
        if count > 5:
            count = 0
            break
        orders_list.append(order_)
    for customer_ in customers:
        if count > 5:
            break
        customers_list.append(customer_)


    context = {
        "orders_delivered": orders.filter(status="Delivered"),
        "orders_pending":orders.filter(status="Pending"),
        "orders":orders,
        "customers":customers,
        "customers_list":customers_list,
        "orders_list":orders_list,
    }
    return render(request, "accounts/dashboard.html", context)

########################
## products views

@login_required
@is_allowed(["admins"])
def products(request):
    products_all = Product.objects.all().order_by("name")
    context = {
        "products_all":products_all
    }
    return render(request, "accounts/product/products.html", context)

@login_required
@is_allowed(["admins"])
def CreateProductView(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Product created Successfully")
            return redirect("products")
    else:
        form = ProductForm()
    context = {"form":form}
    return render(request, "accounts/product/create_product.html", context)

@login_required
@is_allowed(["admins"])
def UpdateProductView(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Product Updated Successfully")
            return redirect("products")
    else:
        form = ProductForm(instance=product)
    context = {"form":form}
    return render(request, "accounts/product/update_product.html", context)

@login_required
@is_allowed(["admins"])
def DeleteProductView(request, pk):
    product = get_object_or_404(Product, id = pk)
    if request.method == "POST":
        Product.delete(product)
        messages.add_message(request, messages.SUCCESS, "Product delete Successfully")
        return redirect("products")
    context = {"object_name":"Product",
               "afterObjName":f'With Name "{product.name}"'
               }
    return render(request, "accounts/delete_confirmation.html", context)

###################
#### Customer Views
@login_required
@is_allowed(["admins"])
def customerPage(request, customer_id):
    needed_customer = get_object_or_404(Customer, id = customer_id)
    orders = needed_customer.order_set.all().order_by("-date_created")
    filter_orders = OrderFilter(data= request.GET, queryset=orders)
    orders = filter_orders.qs
    return render(request, "accounts/customer/customer.html", {"needed_customer":needed_customer, "orders":orders, "filter_orders":filter_orders})

@login_required
@is_allowed(["admins"])
def CreateCustomerView(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Customer created Successfully")
            return redirect("customerPage", form.instance.id)
    else:
        form = CustomerForm()
    context = {"form":form}
    return render(request, "accounts/customer/create_customer.html", context)

@login_required
@is_allowed(["admins"])
def UpdateCustomerView(request, pk):
    customer = get_object_or_404(Customer, id = pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Customer Updated Successfully")
            return redirect("customerPage", customer.id)
    else:
        form = CustomerForm(instance=customer)
    context = {"form":form}
    return render(request, "accounts/product/update_product.html", context)

@login_required
@is_allowed(["admins"])
def DeleteCustomerView(request, pk):
    customer = get_object_or_404(Customer, id = pk)
    if request.method == "POST":
        Customer.delete(customer)
        messages.add_message(request, messages.SUCCESS, "Customer delete Successfully")
        return redirect("dashboard")

    context = {"object_name":"Product",
               "afterObjName":f'With Name "{customer.name}"',
               'anotherText':"Note That This Will Make Products Buyers To  NULL And Order Of This Customer To NULL Also !"}
    return render(request, "accounts/delete_confirmation.html", context)

####################
## Order Views

@login_required
@is_allowed(["admins"])
def ListOrderView(request):
    orders = Order.objects.all()
    context = {"orders":orders, "orderPrice": 5}
    return render(request, "accounts/order/order_list.html", context)

@login_required
@is_allowed(["admins"])
def UpdateOrderView(request, pk):
    order = get_object_or_404(Order, id = pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            order.date_updated = timezone.now()
            order.save()
            messages.add_message(request, messages.SUCCESS, "Order Updated Successfully")
            return redirect("customerPage", order.customer.id)
    else:
        form = OrderForm(instance=order)
    context = {"form":form}
    return render(request, "accounts/product/update_product.html", context)

@login_required
@is_allowed(["admins"])
def DeleteOrderView(request, pk):
    order = get_object_or_404(Order, id = pk)

    if not order.customer and not order.product:
        afterObjName = f'of {order.customer.name} and with product Name "{order.product.name}"'
    elif order.customer:
        afterObjName = f"of {order.customer.name}"
    elif order.product:
        afterObjName = f'with product Name "{order.product.name}"'
    else:
        afterObjName = f"with product {order}"

    if request.method == "POST":
        Order.delete(order)
        messages.add_message(request, messages.SUCCESS, "Order Delete Successfully")
        return redirect("dashboard")

    context = {"object_name":"Order",
        "afterObjName":afterObjName}
    return render(request, "accounts/delete_confirmation.html", context)

@login_required
@is_allowed(["admins"])
def CreateOrderView(request, customer_id):
    customer = get_object_or_404(Customer, id = customer_id)
    orderFormSet = inlineformset_factory(Customer, Order, fields= ("product","status"), extra=5, can_delete=False)
    if request.method == "POST":
        FormSet = orderFormSet(request.POST, instance = customer)
        if FormSet.is_valid():
            FormSet.save()
            return redirect("customerPage", customer.id)
    else:
        FormSet = orderFormSet()
    return render(request, "accounts/order/create_order.html", {"FormSet":FormSet})