# important imports
from django.shortcuts import redirect, render
from django.http import HttpResponse

# decorators here
def is_not_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def is_allowed(allowed_groups):
    def decoratorFunc(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                group = request.user.groups.all()[0]
                if group in allowed_groups:
                    return view_func(request, *args, **kwargs)
                return redirect("error", "403")
        return wrapper_func
    return decoratorFunc