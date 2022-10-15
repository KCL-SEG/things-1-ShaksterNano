from django.http import HttpResponse
from django.shortcuts import render


def home(request: HttpResponse) -> HttpResponse:
    return render(request, "home.html")
