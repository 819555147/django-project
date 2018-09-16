from django.shortcuts import render, redirect
from django.db import models
import logging
from RegistLog.models import Users
'''
编写响应函数
'''
# Create your views here.


# 登录界面响应函数
def log_in(request):
    un = request.session.get('username')
    if un:
        return redirect('/spider')
    else:
        return render(request, 'login.html')


def logout(request):
    del request.session["username"]
    return render(request, 'login.html')


# 验证响应函数
def validate(request):
    un = request.session.get('username')
    if un:
        return redirect('/spider')
    else:
        username = request.POST.get('username', 'none')
        password = request.POST.get('password', 'none')
        try:
            user = Users.objects.get(Username=username, Password=password)
        except Exception as e:
            logging.info(str(e))
            return render(request, 'login.html', {'info': '密码或用户名错误！', 'style': 'display:block;'})
        request.session['username'] = username
        return redirect('/spider')
