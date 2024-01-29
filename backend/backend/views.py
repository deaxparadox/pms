from django.shortcuts import render, redirect
from django.urls import reverse

def error_404_view(request):
    return render(
        request,
        "404.html"
    )

def dashboard_view(request):
    return render(
        request,
        "home/index.html"
    )

def root_view(request):
    return redirect(reverse("dashboard"))