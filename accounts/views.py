from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, Page
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
########################
## main page
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


########################
## products views
def products(request):
    products_all = Product.objects.all().order_by("name")
    context = {
        "products_all":products_all
    }
    return render(request, "accounts/product/products.html", context)

class CreateProductView(CreateView, SuccessMessageMixin):
    model = Product
    template_name = "accounts/product/create_product.html"
    fields = "__all__"
    success_message = "Product Created Successfully"

class DeleteProductView(DeleteView, SuccessMessageMixin):
    model = Product
    template_name = "accounts/delete_confirmation.html"
    success_message = "Product Delete Successfully"

    def get_context_data(self, *args, **kwargs):
        context = super(DeleteView, self).get_context_data(*args, **kwargs)
        context["object_name"] = "Product"
        context["afterObjName"] = f'With Name "{self.object.name}"'
        return context

    success_url = "/accounts/products"

class UpdateProductView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "accounts/product/update_product.html"
    success_message = "Product Updated Successfully"
    success_url = "/accounts/"

###################
#### Customer Views
def customerPage(request, customer_id):
    needed_customer = get_object_or_404(Customer, id = customer_id)
    orders = needed_customer.order_set.all().order_by("-date_created")
    return render(request, "accounts/customer/customer.html", {"needed_customer":needed_customer, "orders":orders})

class CreateCustomerView(CreateView, SuccessMessageMixin):
    model = Customer
    fields = ["name", "phone", "email"]
    template_name = "accounts/customer/create_customer.html"
    success_message = "Customer Created Successfully"
    success_url = "/accounts/"

class UpdateCustomerView(UpdateView, SuccessMessageMixin):
    model = Customer
    fields = ["name", "phone", "email"]
    template_name = "accounts/customer/update_customer.html"
    success_message = "Customer Updated Successfully"
    success_url = "/accounts/"

class DeleteCustomerView(DeleteView, SuccessMessageMixin):
    model = Customer
    template_name = "accounts/delete_confirmation.html"
    success_message = "Customer Delete Successfully"
    success_url = "/accounts/"

    def get_context_data(self, *args, **kwargs):
        context = super(DeleteView, self).get_context_data(*args, **kwargs)
        context["object_name"] = "Customer"
        context['anotherText'] = "Note That This Will Make Products Buyers To  NULL And Order Of This Customer To NULL Also !"
        context["afterObjName"] = f"With Name : {self.object.name}"
        return context


####################
## Order Views
class ListOrderView(ListView):
    model = Order
    template_name = "accounts/order/order_list.html"
    context_object_name = "orders"
    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        context["orderPrice"] = 5
        return context

class CreateOrderView(CreateView, SuccessMessageMixin):
    model = Order
    fields = ["product", "status"]
    template_name = "accounts/order/create_order.html"
    success_message = "Order Created Successfully"
    success_url = "/accounts/listOrder"

    def form_valid(self, form):
        customer_ = get_object_or_404(Customer, id = self.kwargs['customer_id'])

        form.instance.customer = customer_
        return super().form_valid(form)

class UpdateOrderView(UpdateView, SuccessMessageMixin):
    model = Order
    fields = "__all__"
    template_name = "accounts/order/update_order.html"
    success_message = "Order Updated Successfully"
    success_url = "/accounts/"

class DeleteOrderView(DeleteView, SuccessMessageMixin):
    model = Order
    template_name = "accounts/delete_confirmation.html"
    success_message = "Order Delete Successfully"

    def get_context_data(self, *args, **kwargs):
        context = super(DeleteView, self).get_context_data(*args, **kwargs)
        context["object_name"] = "Order"
        if not self.object.customer and not self.object.product:
            context["afterObjName"] = f'of {self.object.customer.name} and with product Name "{self.object.product.name}"'
        elif self.object.customer:
            context["afterObjName"] = f"of {self.object.customer.name}"
        elif self.object.product:
            context["afterObjName"] = f'with product Name "{self.object.product.name}"'
        else:
            context["afterObjName"] = f"with product {self.object}"
        return context

    success_url = "/accounts/"
