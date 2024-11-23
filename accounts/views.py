from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空表单
        form = UserCreationForm()
    else:
        # 处理提交的表单
        form  = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 自动登入重定向到主页
            login(request, new_user)
            return redirect('WebWithLogin:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


