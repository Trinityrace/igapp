from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http  import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt

# Create your views here.

def signup(request):
    context = {}
    return render(request, 'sign-up.html', context)

def index(request):
    context = {}
    return render(request, 'index.html', context)
