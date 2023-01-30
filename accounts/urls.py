from django.urls import path
from . import views
urlpatterns = [
    path("", views.dashBoard, name = "dashboard"),
    path("products/", views.products, name = "products"),
    path("customer/<int:customer_id>/", views.customerPage, name = "customerPage"),
    path("createCustomer/", views.CreateCustomerView.as_view(), name = "createCustomer"),
    path("updateCustomer/<int:pk>", views.UpdateCustomerView.as_view(), name = "updateCustomer"),
    path("deleteCustomer/<int:pk>", views.DeleteCustomerView.as_view(), name = "deleteCustomer"),
]