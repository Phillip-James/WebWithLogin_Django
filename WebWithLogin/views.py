from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("show the items")

def detail(request, Item_id):
    return HttpResponse(f"detail item{Item_id}")