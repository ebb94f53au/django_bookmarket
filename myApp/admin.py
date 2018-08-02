from django.contrib import admin
from .models import *
# Register your models here.



class WheelAdmin(admin.ModelAdmin):
    list_display = ('img','name','bookid','isDelete')

class MustbuyAdmin(admin.ModelAdmin):
    list_display = ('img', 'name', 'bookid', 'isDelete')

class NavAdmin(admin.ModelAdmin):
    list_display = ('img','name','url')

class UserAdmin(admin.ModelAdmin):
    list_display = ('userAccount','userPasswd',
                    'userName','userPhone','userAdderss','userImg','userRank','userToken')

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'bookid', 'booktype',
                    'img','price','mprice','info','nums','salesnums','iswonderf','isDelete')

class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('typename', 'isDelete')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user','book','booknum','isChose','order','isDelete')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('userAccount','token','remarks','isDelete')
admin.site.register(Wheel,WheelAdmin)
admin.site.register(Nav,NavAdmin)
admin.site.register(Mustbuy,MustbuyAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(BookType,BookTypeAdmin)
admin.site.register(Cart,CartAdmin,list_filter=['isDelete'])
admin.site.register(Order,OrderAdmin)