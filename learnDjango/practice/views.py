from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myName(request):
    return HttpResponse('My Name is Foysal Ahmed')