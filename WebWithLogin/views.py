from cProfile import Profile

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Item, subscribed_items, profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
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

@login_required(login_url="/accounts/login/")
def profile_page(request):
    """展示个人信息和订阅信息"""
    subscribed_item_list = subscribed_items.objects.filter(user_id=request.user).order_by('overtime')
    for sub_item in subscribed_item_list:
        sub_item.overtime_judge()
    username = request.user.username
    try:
        userprofile = profile.objects.get(user_id=request.user.id)
    except profile.DoesNotExist:
        raise Http404("User's profile does not exist")

    content = {"username": username, "userprofile": userprofile, "subscribed_items": subscribed_item_list}
    return render(request, 'WebWithLogin/profile.html', content)


@login_required(login_url="/accounts/login/")
def subscribe_item(request, Item_id):
    # 获取item信息
    if request.method == 'POST':
        if "confirm" in request.POST:
            if subscribed_items.objects.filter(user_id=request.user.id, item_id=Item_id).exists():
                if profile.objects.get(user_id=request.user.id).last_money <= Item.objects.get(pk=Item_id).price:
                    return render(request, "WebWithLogin/sub_result.html", {"message": "余额不足"})
                else:
                    return render(request, "WebWithLogin/sub_result.html", {"message":"您已订阅过该项目"})

            subscribed_items.objects.create(user=request.user, item=Item.objects.get(pk=Item_id))

            return render(request, "WebWithLogin/sub_result.html", {"message":"订阅成功"})
        return render(request, "WebWithLogin/sub_result.html", {"message":"已取消"})
    return render(request, "WebWithLogin/confirm.html", {"item": Item.objects.get(pk=Item_id), "profile":profile.objects.get(user_id=request.user.id)})


@login_required(login_url="/accounts/login/")
def change_profile(request, user_id=None):
    """更改profile介绍"""
    intro = profile.objects.get(user_id=request.user.id)
    if request.method != 'POST':
        form = ProfileForm(instance=intro)
    else:
        form = ProfileForm(instance=intro, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('WebWithLogin:profile_page')

    context = {'form': form, 'profile': profile.objects.get(user_id=request.user.id)}
    return render(request, 'WebWithLogin/change_profile.html', context)
