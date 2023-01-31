from django.urls import path
from . import views
urlpatterns = [
    path("", views.dashBoard, name = "dashboard"),
    path("products/", views.products, name = "products"),
    path("createProduct/", views.CreateProductView.as_view(), name = "createProduct"),
    path("deleteProduct/<int:pk>", views.DeleteProductView.as_view(), name="deleteProduct"),
    path("updateProduct/<int:pk>", views.UpdateProductView.as_view(), name="updateProduct"),

    path("customer/<int:customer_id>/", views.customerPage, name = "customerPage"),
    path("createCustomer/", views.CreateCustomerView.as_view(), name = "createCustomer"),
    path("updateCustomer/<int:pk>", views.UpdateCustomerView.as_view(), name = "updateCustomer"),
    path("deleteCustomer/<int:pk>", views.DeleteCustomerView.as_view(), name = "deleteCustomer"),

    path("createOrder/<int:customer_id>", views.CreateOrderView.as_view(), name = "createOrder"),
    path("updateOrder/<int:pk>", views.UpdateOrderView.as_view(), name = "updateOrder"),
    path("deleteOrder/<int:pk>", views.DeleteOrderView.as_view(), name = "deleteOrder"),
    path("listOrder/", views.ListOrderView.as_view(), name = "listOrder"),
]