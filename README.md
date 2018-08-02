# django_bookmarket
图书售卖系统，简单来说是类似与网上商城的系统。
此项目为手机端，电脑网页打开F12选择适用手机
现只实现功能：账号注册及登录，图书首页显示、top10排行，图书购买购物车、订单的操作及查询。
测试数据在 myApp/ 下的data.txt 与 type.txt

运行操作  

下载代码后setting文件中更改数据库配置，并且本地创建相同数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'你的数据库名',
        'USER':'账号',
        'PASSWORD':'密码',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

到项目根目录,关联数据库
1.python manage.py makemigrations 
2.python manage.py migrate

将测试数据data.txt 与 type.txt用 mysql导入

创建后台用户
python manage.py createsuperuser

运行项目
python manage.py  runserver

 
