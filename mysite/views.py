from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('thi is about page')

def home(request):
    return render(request, 'home.html', {'greeting': 'Hi'})

def reverse(request):
    return render(request, 'reverse.html', {'greeting': 'This is reverce'})