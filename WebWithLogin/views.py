from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

# Create your views here.

def index(request):
    Item_recommended_list = Item.objects.filter(recommended=True)
    template = loader.get_template("index.html")
    context = {
        "Item_recommended_list": Item_recommended_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, Item_id):
    return HttpResponse(f"detail item{Item_id}")