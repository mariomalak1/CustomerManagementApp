from django.urls import path
from . import views
urlpatterns = [
    path("", views.dashBoard, name = "dashboard"),
    path("products/", views.products, name = "products"),
    path("createProduct/", views.CreateProductView, name = "createProduct"),
    path("deleteProduct/<int:pk>", views.DeleteProductView, name="deleteProduct"),
    path("updateProduct/<int:product_id>", views.UpdateProductView, name="updateProduct"),

    path("customer/<int:customer_id>/", views.customerPage, name = "customerPage"),
    path("createCustomer/", views.CreateCustomerView, name = "createCustomer"),
    path("updateCustomer/<int:pk>", views.UpdateCustomerView, name = "updateCustomer"),
    path("deleteCustomer/<int:pk>", views.DeleteCustomerView, name = "deleteCustomer"),

    path("createOrder/<int:customer_id>", views.CreateOrderView, name = "createOrder"),
    path("updateOrder/<int:pk>", views.UpdateOrderView, name = "updateOrder"),
    path("deleteOrder/<int:pk>", views.DeleteOrderView, name = "deleteOrder"),
    path("listOrder/", views.ListOrderView, name = "listOrder"),
]