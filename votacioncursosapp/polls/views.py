from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#creación de función index
def index(request):
    return HttpResponse('Hello World')