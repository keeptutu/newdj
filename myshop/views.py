from django.shortcuts import render,redirect,HttpResponse
from . import models
from .models import Goods,User

import json

# Create your views here.


def index(request):
    is_login = request.COOKIES.get('is_login')

    goodname = Goods.objects.filter()
    data = {}
    for good in goodname:
        data.update({good.goods_id:{'good_name':good.goods_name,
                                    'good_price': good.good_price,
                                    'good_id': good.goods_id,
                                    'good_img_id': good.good_img_id,
                                    'good_tags': good.tags,
                                    'stock':good.stock,

                                    }})
    # print(data)

    #   goods_id) 商品id
    #   goods_name) 商品名字
    #   good_price) 商品价格
    #   good_img_id) 商品图片id
    #   tags) 商品分类标签

    res = render(request, 'myshop/index.html', {'is_login': is_login,
                                                'good': json.dumps(data)})


    return res


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # massage = '必须填写所有字段'
        if username and password:
            username = username.strip()

            try:
                user = models.User.objects.get(name=username)
            except:
                return render(request, 'myshop/login.html')
            if user.password == password:
                res = redirect('/shop')
                res.set_cookie('is_login', 1)
                return res

    return render(request, 'myshop/login.html')


def details(request,good_id):
    goods_info = Goods.objects.get(goods_id=good_id)
    print(goods_info)

    return render(request,'myshop/details.html',{'good_info':goods_info})


def cart(request):
    return HttpResponse('gouwuche')


def user_zone(request,user_id):
    name = User.objects.get(id=user_id)
    return HttpResponse('user')