from django.urls import path
from .views import *
urlpatterns = [
    path("<str:error_name>/", handelError, name = "error"),
]