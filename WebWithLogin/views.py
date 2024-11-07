from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Item

# Create your views here.

def index(request):
    Item_recommended_list = Item.objects.filter(recommended=True)
    template = loader.get_template("WebWithLogin/index.html")
    context = {
        "Item_recommended_list": Item_recommended_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "WebWithLogin/index.html", context)

def detail(request, Item_id):
    try:
        item = Item.objects.get(pk=Item_id)
    except item.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, "WebWithLogin/detail.html", {"item": item})

    #another way
    #item = get_object_or_404(Item, pk = Item_id)
    #return render(request, "template_name", {})
