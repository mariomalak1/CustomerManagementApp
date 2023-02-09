import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    date_start__gt = django_filters.DateFilter(field_name= "from_date", lookup_expr= "gt")
    date_end__lt = django_filters.DateFilter(field_name= "to_date", lookup_expr= "lt")
    class Meta:
        model = Order
        fields = "__all__"
