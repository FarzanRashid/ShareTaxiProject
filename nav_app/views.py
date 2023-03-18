from django.shortcuts import render
from django.http import HttpResponse
from .forms import GetUserInfoForm


def index(request):
    return HttpResponse("<h1>Welcome to ShareTaxi.</h1>")


def book_taxi(request):
    if request.method == "POST":
        form = GetUserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'nav_app/success.html')
    else:
        form = GetUserInfoForm()
    return render(request, 'nav_app/nav_app.html', {'form': form})