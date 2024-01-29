from django.urls import reverse
from django.shortcuts import redirect

def pms_home_to_redirect(request):
    return redirect(reverse("pms:home"))