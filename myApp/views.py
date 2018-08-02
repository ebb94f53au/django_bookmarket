from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *

# Create your views here.
def home(request):
    #将滚屏传到home界面
    wheelList=Wheel.objects.all()
    # 将功能传到home界面
    navList=Nav.objects.all()[:4]
    # 将必买传到home界面
    mustbuyList=Mustbuy.objects.all()
    # 将top10传到home界面
    top10_list=Book.objects.order_by('salesnums')[::-1][:10]

    return render(request,'bookmarket/home.html',
                  {'title':'home',
                   'wheelList':wheelList,
                   'navList':navList,
                   'mustbuyList':mustbuyList,
                   'top10_list':top10_list,
                   })
def market(request,type,sort):
    #先判断书的类型
    if type!=0:
        booktype=BookType.objects.get(id=type)
        BookList=Book.objects.filter(booktype=booktype)
    else:
        BookList = Book.objects.all()
    #再判断书的排序顺序
    if sort == 1:
        BookList = BookList.order_by('salesnums')[::-1]
    elif sort == 2:
        BookList = BookList.order_by('price')
    elif sort == 3:
        BookList = BookList.order_by('price')[::-1]

    leftTypeList=BookType.objects.all()
    return render(request,'bookmarket/market.html',
                  {'title':'market',
                    'typeid':type,
                    'sort':sort,
                   'leftTypeList':leftTypeList,
                   'BookList':BookList
                   })
def cart(request):
    #输出用户账号，购物车信息
    userAccount=request.session.get('userAccount',None)
    try:
        user=User.objects.get(userAccount=userAccount)
        cartList=Cart.objects.filter(user=user,isDelete=False)
    except:
        user=None
        cartList=None
    return render(request,'bookmarket/cart.html',
                  {'title':'cart',
                   'user':user,
                   'cartList':cartList
                   })

def changecart(request,type):
    #修改购物车操作    加商品减商品  单选商品 全选商品
    bookid = request.POST.get('bookid', None)
    book = Book.objects.get(bookid=bookid)
    try:
        userAccount = request.session.get('userAccount')
        user=User.objects.get(userAccount=userAccount)
    except:
        return JsonResponse({'status': 'error','data':-1})
    if type==0:
        # 加
        try:
            cart=Cart.objects.get(user=user,book=book,isDelete=False)
            book.nums = book.nums - 1
            if book.nums>=0:
                cart.booknum=cart.booknum+1
                price=book.price*cart.booknum
                num=cart.booknum
                book.save()
                cart.save()
            else:
                return  JsonResponse({'status': 'error'})
        except:
            num=1
            cart=Cart.createcart(user,book,num)
            price=book.price
            cart.save()
        return JsonResponse({'status': 'success',
                             'data': num,
                             'price': price,

                             })
    elif type==1:
        #减
        try:
            cart = Cart.objects.get(user=user, book=book,isDelete=False)
            cart.booknum = cart.booknum -1
            price = book.price * cart.booknum
            if cart.booknum==0:
                cart.isDelete=True
            num=cart.booknum
            cart.save()
        except:
            num=0
            price=0
        return JsonResponse({'status': 'success',
                             'data': num,
                             'price': price,

                             })
    elif type==2:
        #ischeck 的判断
        try:
            cart = Cart.objects.get(user=user, book=book,isDelete=False)
            if cart.isChose:
                cart.isChose=False
                cart.save()
                return JsonResponse({'status': 'success',
                                     'data': ' ',
                                     })
            else:
                cart.isChose = True
                cart.save()
                return JsonResponse({'status': 'success',
                                     'data': '√',
                                     })

        except:
            return JsonResponse({'status': 'error'})
    elif type==3:
        #allchose 为true
        try:
            cart = Cart.objects.get(user=user, book=book,isDelete=False)

            if not cart.isChose:
                #将ischose 为false全部变为true
                cart.isChose = True
                cart.save()
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error'})

    elif type == 4:
        # allchose 为false
        try:
            cart = Cart.objects.get(user=user, book=book)

            if cart.isChose:
              # 将ischose 为true全部变为false
                cart.isChose = False
                cart.save()
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error'})
import json
def saveorder(request):
    # 将购物车转换为订单
    if request.method=='POST':
        try:
            remarks=request.POST.get('remarks')
            userAccount=request.session.get('userAccount')
            user=User.objects.get(userAccount=userAccount)
            order=Order.creatorder(userAccount,time.time(),remarks)
            order.save()
            carts=Cart.objects.filter(user=user,isChose=True,isDelete=False)
            for cart in carts:
                cart.order=order
                cart.isDelete=True
                cart.save()
            return JsonResponse({'status':'success'})
        except:
            return JsonResponse({'status': 'error'})

    else:
        return JsonResponse({'status': 'error'})

def mine(request):
    #取用户信息
    userAccount=request.session.get('userAccount',None)
    try:
        user=User.objects.get(userAccount=userAccount)
        username = user.userName
        userImg = user.userImg
        userRank=user.userRank
    except:
        username = '未登录,请点此登录。'
        userImg = 'base'
        userRank = 0

    return render(request,'bookmarket/mine.html',
                  {'title':'mine',
                   'username':username,
                    'userImg':userImg,
                    'userRank':userRank
                   })

import os
from django.conf import settings
import time
def register(request):
    #注册 如果取不到值则为进去页面，取到账号值 则为注册
    #写一个错误页面跳转
    userAccount=request.POST.get('userAccount',None)
    if userAccount== None:
        return render(request,'bookmarket/register.html',{'title':'register'})
    else:
        userPass = request.POST.get('userPass')
        userName = request.POST.get('userName')
        userPhone = request.POST.get('userPhone')
        userAddress = request.POST.get('userAddress')
        #将图片文件存到本地static/meida/文件夹下
        userImg = request.FILES['userImg']
        imgPath=os.path.join(settings.MEDIA_ROOT,userAccount+'.png')
        with open(imgPath,'wb') as f:
            for i in userImg.chunks():
                f.write(i)
        userImg='media/'+userAccount+'.png'
        userRank=0
        userToken=time.time()
        #创建新用户
        a=User.createUser(userAccount,userPass,userName,userPhone,userAddress,userImg,userRank,userToken)
        User.save(self=a)
        #将账号存到session中
        request.session["userAccount"] = userAccount
        return redirect('/mine/')

def checkuserid(request):
    #js jquery .post调用 查询数据库是否账号名重复
    account=request.POST.get('userid',None)
    try:
        User.objects.get(userAccount=account)
        status='error'
    except:
        status = 'success'

    return JsonResponse({'status':status})

from .Form.loginForm import loginform
def login(request):
    #登录界面
    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
                user=User.objects.get(userAccount=username)
                if password != user.userPasswd:
                    return redirect('/login/')
            except:
                return redirect('/login/')
            #成功登陆
            token = time.time()
            user.userToken = str(token)
            user.save()
            request.session["userAccount"] = username
            return redirect('/mine/')
        else:
            return render(request, 'bookmarket/login.html', {'title': 'login', 'forms': form,'error':form.errors})
    else:
        form = loginform()
        return render(request,'bookmarket/login.html',{'title':'login','forms':form})
def quit(request):
    request.session.clear()
    return redirect('/mine/')

def modify(request,type):
    #修改用户信息
    try:
        userAccount = request.session.get('userAccount', None)
        user = User.objects.get(userAccount=userAccount)
    except:
        return redirect('/login/')
    if type==0:
        #修改用户 地址 电话 地址
        if request.method=="GET":
            return render(request, 'bookmarket/modify_cart.html', {'user': user})

        else:
            username = request.POST.get('userName', None)
            userPhone = request.POST.get('userPhone', None)
            userAddress = request.POST.get('userAddress', None)
            if username==None or username==None or username==None:
                return render(request, 'bookmarket/modify_cart.html', {'user': user})
            else:
                user.userName=username
                user.userPhone=userPhone
                user.userAdderss=userAddress
                user.save()
                return redirect('/cart/')
    if type==1:
        #更改头像
        if request.method == "GET":
            return render(request, 'bookmarket/modify_img.html')
        else:
            # 将图片文件存到本地static/meida/文件夹下
            userImg = request.FILES['userImg']
            imgPath = os.path.join(settings.MEDIA_ROOT, userAccount + '.png')
            with open(imgPath, 'wb') as f:
                for i in userImg.chunks():
                    f.write(i)
            return redirect('/mine/')

def show_orders(request):
    try:
        userAccount=request.session.get('userAccount',None)
        orders= Order.objects.filter(userAccount=userAccount,isDelete=False)
    except:
        return redirect('/login/')

    if request.method=='POST':
       token= request.POST.get('token',None)
       if token!=None:
            order=Order.objects.get(userAccount=userAccount,isDelete=False,token=token)
            order.isDelete=True
            order.save()
            return JsonResponse({'status':'success'})
       else:
           return JsonResponse({'status':'error'})

    else:
        return render(request,'bookmarket/show_orders.html',{'title':'全部订单','orders':orders})


