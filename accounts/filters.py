import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    date_start = django_filters.DateFilter(field_name= "from date", lookup_expr= "gt")
    date_end = django_filters.DateFilter(field_name= "to date", lookup_expr= "lt")
    class Meta:
        model = Order
        fields = ["product", "status"]
        # execlud =