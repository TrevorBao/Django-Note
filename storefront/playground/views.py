from django.shortcuts import render
from django.http import HttpResponse


def Calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    x = Calculate()
    return render(request, 'hello.html', {'name': 'Mosh'})
