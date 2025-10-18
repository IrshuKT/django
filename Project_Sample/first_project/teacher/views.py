from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def teacher(request):
    return render(request ,'teacher.html')