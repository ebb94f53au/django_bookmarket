# Generated by Django 2.0.7 on 2018-07-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20180724_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='userAccount',
            field=models.CharField(default=None, max_length=50, verbose_name='用户账号名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='userToken',
            field=models.CharField(max_length=50, verbose_name='token验证值'),
        ),
    ]