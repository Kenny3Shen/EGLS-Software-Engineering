from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
import json
from .models import UserFavoritesLinks


# Create your views here.
class SignHandler:
    def handle(self, request):
        param_dict = json.loads(request.body)
        action = param_dict.get('action')
        request.pd = param_dict
        if action == 'signin':
            return self.signin(request)
        elif action == 'signout':
            return self.signout(request)
        else:
            return {'ret': -1, 'msg': 'params error'}

    def signin(self, request):
        # 从 HTTP POST 请求中获取用户名、密码参数
        userName = request.pd.get('username')
        passWord = request.pd.get('password')

        # 使用 Django auth 库里面的 方法校验用户名、密码
        user = authenticate(username=userName, password=passWord)

        # 如果能找到用户，并且密码正确
        if user is None:
            return JsonResponse({'ret': 1, 'msg': 'Wrong username or password'})

        login(request, user)
        return JsonResponse(
            {
                'ret': 0,
                'msg': 'Login successful',
                'username': user.username
            }
        )

    # 登出处理
    def signout(self, request):
        # 使用登出方法
        logout(request)
        return JsonResponse({'ret': 0})


class ItemHandle:
    def handle(self, request):
        if request.method == 'GET':  # get item
            pd = request.GET
        else:  # add or del
            pd = json.loads(request.body)

        action = pd.get('action')

        if action == 'addItem':
            return self.addItem(request)
        elif action == 'delItem':
            return self.delItem(request)
        elif action == 'getAllItems':
            return self.getAllItems(request)

    def addItem(self, request):
        data = request.pd.get('data')
        item = UserFavoritesLinks.objects.create(

        )
    def delItem(self, request):
        pass

    def getAllItems(self, request):
        pass
