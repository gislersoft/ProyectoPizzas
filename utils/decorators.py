from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect


def auth_check_msg(
    users,
    login_url="login",
    redirects="home",
    login_msg="Debes iniciar sesión.",
    forbidden_msg=f"No puedes acceder a esta página",
):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request):
            if not request.user.is_authenticated:
                messages.error(request, login_msg)
                return redirect(login_url)
            if request.user.user_type not in users:
                messages.error(request, forbidden_msg)
                return redirect(redirects)
            return view_func(request)

        return wrapper

    return decorator
