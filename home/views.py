from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render (request, 'index.html')

    