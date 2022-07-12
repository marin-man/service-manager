from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField('用户id', primary_key=True, max_length=15)
    username = models.CharField('用户昵称', max_length=20, null=False)
    password = models.CharField('密码', null=False)

    class Meta:
        db_table = 'user'
