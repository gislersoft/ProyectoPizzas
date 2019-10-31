from django.shortcuts import redirect
from django.urls import reverse


class FranchiseValidityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path != reverse("franchise_unavailable"):
            if request.tenant.schema_name != "public" and request.tenant.is_available() is False:
                return redirect("franchise_unavailable")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response