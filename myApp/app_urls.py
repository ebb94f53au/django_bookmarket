from django.contrib import admin
from django.urls import path,include
from myApp import app_urls
from myApp.views import *
app_name='bookmarket'
urlpatterns = [
    path('',home),
    path('home/',home,name='home'),
    path('market/<int:type>/<int:sort>/',market,name='market'),
    path('cart/',cart,name='cart'),
    path('changecart/<int:type>/',changecart,name='changecart'),
    path('saveorder/',saveorder,name='saveorder'),
    path('mine/',mine,name='mine'),
    path('register/',register,name='register'),
    path('checkuserid/',checkuserid,name='checkuserid'),
    path('login/',login,name='login'),
    path('quit/',quit,name='quit'),
    path('modify/<int:type>/',modify,name='modify'),
    path('show_orders/',show_orders,name='show_orders'),



]
