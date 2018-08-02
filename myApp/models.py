from django.db import models

# Create your models here.
class Wheel(models.Model):
    #滚屏轮播类
    img=models.CharField(max_length=150,verbose_name='图片地址')#图片地址
    name=models.CharField(max_length=25,verbose_name='书名')#书名字
    bookid=models.CharField(max_length=10,verbose_name='书id')#书id
    isDelete=models.BooleanField(default=False,verbose_name='逻辑删除')#逻辑删除

class Nav(models.Model):
    #功能选项
    img = models.CharField(max_length=200,verbose_name='图片地址')#图片网络地址
    name = models.CharField(max_length=25,verbose_name='栏目名')#名字
    url = models.CharField(max_length=200,verbose_name='栏目地址')#书id号码

class Mustbuy(models.Model):
    # 每日必抢模型
    img = models.CharField(max_length=200,verbose_name='图片地址')#图片网络地址
    name = models.CharField(max_length=25,verbose_name='书名')#名字
    bookid = models.CharField(max_length=20,verbose_name='书id')#书id号码
    isDelete = models.BooleanField(default=False,verbose_name='逻辑删除')  # 逻辑删除


class BookType(models.Model):
    #书的种类
    typename = models.CharField(max_length=20,verbose_name='书类别名')  # 书类别名
    isDelete = models.BooleanField(default=False,verbose_name='逻辑删除')  # 逻辑删除

    def __str__(self):
        return self.typename
class Book(models.Model):
    #书详情
    name=models.CharField(max_length=25,verbose_name='书名')#书名

    bookid=models.CharField(max_length=20,verbose_name='书id')#书id号码

    #typeid=models.CharField(max_length=20,verbose_name='书类别id')#书类别id

    booktype=models.ForeignKey(BookType,default=None,on_delete=models.PROTECT,verbose_name='书类别')#书类别

    img=models.CharField(max_length=200,verbose_name='图片地址')#书图片地址

    price=models.FloatField(max_length=20,verbose_name='书价格')#书价格

    mprice=models.FloatField(max_length=20,verbose_name='书市场价')#书市场价

    info=models.CharField(max_length=250,verbose_name='书详细介绍')#书详细介绍

    nums=models.IntegerField(verbose_name='书库存')#书库存

    salesnums=models.IntegerField(verbose_name='销量')#销量

    iswonderf=models.BooleanField(default=False,verbose_name='是否精选')#是否精选

    isDelete = models.BooleanField(default=False,verbose_name='逻辑删除')  # 逻辑删除

    def __str__(self):
        return self.name

class User(models.Model):

    userAccount = models.CharField(max_length=20,unique=True,verbose_name='用户账号')# 用户账号，要唯一

    userPasswd  = models.CharField(max_length=20,verbose_name='密码')    # 密码

    userName    =  models.CharField(max_length=20,verbose_name='昵称')    # 昵称

    userPhone   = models.CharField(max_length=20,verbose_name='手机号')    # 手机号

    userAdderss = models.CharField(max_length=100,verbose_name='地址')    # 地址

    userImg     = models.CharField(max_length=150,verbose_name='头像路径')    # 头像路径

    userRank    = models.IntegerField(default=0,verbose_name='等级')    # 等级

    userToken   = models.CharField(max_length=50,verbose_name='token验证值')    # touken验证值，每次登陆之后都会更新

    def __str__(self):
        return self.userAccount
    @classmethod
    def createUser(cls,account,passwd,name,phone,address,img,rank,token):
        u = cls(userAccount = account,userPasswd = passwd,userName=name,userPhone=phone,userAdderss=address,userImg=img,userRank=rank,userToken=token)
        return u


#设置objects过滤条件，isDelete=False的显示
class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1,self).get_queryset().filter(isDelete=False)
#设置objects过滤条件，isChose=False的显示
class CartManager2(models.Manager):
    def get_queryset(self):
        return super(CartManager2,self).get_queryset().filter(isChose=True)

class Order(models.Model):
    #一个订单由多个购物车组成,一对多
    userAccount=models.CharField(max_length=50,verbose_name='用户账号名') #用户账号名

    token=models.CharField(max_length=50,verbose_name='订单时间') #订单时间

    remarks=models.CharField(max_length=200,default=None,verbose_name='备注')#备注

    isDelete = models.BooleanField(default=False,verbose_name='逻辑删除')#逻辑删除
    def __str__(self):
        return self.token
    @classmethod
    def creatorder(cls,userAccount, token,remarks):
        order = cls(userAccount=userAccount,token=token,remarks=remarks)
        return order

class Cart(models.Model):
    #购物车订单购买成功转换为order，多对一
    #PROTECT 外键删除后保护 CASCADE    外键删除后删除
    user = models.ForeignKey(User,default=None,verbose_name='用户',null=True,on_delete=models.CASCADE)  # 用户

    book = models.ForeignKey(Book,default=None,verbose_name='书',on_delete=models.CASCADE)  # 书

    booknum = models.IntegerField(verbose_name='书数量')#书数量

    isChose = models.BooleanField(default=False,verbose_name='是否选择')#是否选择

    # isOrder = models.BooleanField(default=False,verbose_name='是否变为订单')#是否变为订单

    order = models.ForeignKey(Order,default=None,verbose_name='订单',on_delete=models.CASCADE,null=True)#订单

    isDelete = models.BooleanField(default=False,verbose_name='逻辑删除')#逻辑删除
    #自定义模型管理器
    #
    def __str__(self):
        return self.user.userName+','+self.book.name
    # objects = CartManager1()
    # #objects1 = CartManager1()
    # objects2 = CartManager2()
    #查看订单
    #object2 = CartManager2()
    @classmethod
    def createcart(cls,user,book,booknum,order=None):
        c = cls(user = user,book= book,booknum=booknum,order=order)
        return c

# class Cart(models.Model):
#     #购物车订单购买成功转换为order
#
#     userAccount = models.CharField(max_length=20,verbose_name='用户名')#用户名
#
#     bookid = models.CharField(max_length=10,verbose_name='书id')#书id
#
#     booknum = models.IntegerField(verbose_name='书数量')#书数量
#
#     bookprice = models.FloatField(verbose_name='书价格')#书价格
#
#     isChose = models.BooleanField(default=False,verbose_name='是否选择')#是否选择
#
#     bookimg = models.CharField(max_length=150,verbose_name='书图片地址')#书图片地址
#
#     bookname = models.CharField(max_length=100,verbose_name='书名')#书名
#
#     orderid = models.CharField(max_length=20,default="0",verbose_name='订单号')#订单号
#
#     isDelete = models.BooleanField(default=False,verbose_name='逻辑删除')#逻辑删除
#     #自定义模型管理器
#     #
#     objects = CartManager1()
#     #查看订单
#     #object2 = CartManager2()
#     @classmethod
#     def createcart(cls,userAccount,bookid,booknum,bookprice,bookimg,bookname):
#         c = cls(userAccount = userAccount,bookid = bookid,booknum=booknum,
#                 bookprice=bookprice,bookimg=bookimg,bookname=bookname)
#         return c

# class Order(models.Model):
#     #订单2个外键 用户 额
#
#     user = models.ForeignKeyField(User, verbose_name='用户名')  # 用户
#
#     book = models.ForeignKeyField(Book, verbose_name='书id')  # 书
#
#     booknum = models.IntegerField(verbose_name='书数量')  # 书数量
#
#     token=models.CharField(max_length=50,verbose_name='订单时间') #订单时间
#
#     isDelete = models.BooleanField(default=False,verbose_name='逻辑删除')#逻辑删除
#
#     @classmethod
#     def creatorder(cls, orderid, userid, progress):
#         order = cls(orderid=orderid, userid=userid, progress=progress)
#         return order