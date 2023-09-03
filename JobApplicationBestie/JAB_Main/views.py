from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    return render(request, 'JAB_Main/home.html', {})
