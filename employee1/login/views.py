from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.models import User  # django封装好的验证功能
from django.http import JsonResponse
import json


def index(request):
    pass


def status(request):
    if request.user.is_authenticated:
        return JsonResponse({
            "code": "ok",
            "first_name": request.user.first_name
        })
    else:
        return JsonResponse({
            "code": "no"
        })


#  登陆  /api/login
def loging(request):
    tableData = json.loads(request.body)
    # user = tableData['username']
    # pwd = tableData['password']
    try:
        user = tableData['username']
        pwd = tableData['password']
        # 验证密码
        obj = auth.authenticate(request, username=user, password=pwd)
        if obj:
            login(request, obj)
            return JsonResponse({'code': 'ok', 'message': '账号密码验证成功',"first_name": obj.first_name})
        else:
            return JsonResponse({"code": "no", "message": "账号或者密码错误","first_name":"500"})

    except:
        return JsonResponse({'code': 'no', 'message': '验证失败'})


#  注册  /api/register
def register(request):
    try:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = User.objects.create_user(username=username, password=password)
        user.save()
    except:
        return JsonResponse({'code': 'no', 'message': '注册失败'})
    return JsonResponse({'code': 'ok', 'message': '注册成功'})


# 注销  /api/logout
def logouting(request):
    logout(request)
    return JsonResponse({"status": 0})