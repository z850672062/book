from django.db import models

# Create your models here.
#创建book类对应 book表
class Book(models.Model):
    title=models.CharField(max_length=30,unique=True,verbose_name='书名')
    public=models.CharField(max_length=50,verbose_name='出版社')
    price=models.DecimalField(max_digits=7,decimal_places=2,verbose_name='定价')
    def default_price(self):
        return '￥30'
    retail_price=models.DecimalField(max_digits=7,decimal_places=2,verbose_name='零售价',default=default_price)

    def __str__(self):
        return 'titel:%s pub:%s price:%s' % (self.title,self.public,self.price)

#创建作者表
class Author(models.Model):
    name=models.CharField(max_length=30,verbose_name='姓名')
    email=models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return '作者:%s' % (self.name)

#创建用户信息表
class UserInfo(models.Model):
    username=models.CharField(max_length=24,verbose_name='用户注册')
    password=models.CharField(max_length=24,verbose_name='密码')
    # 定义chocies参数的对应关系，以元组（或者列表）的形式进行表述：
    choices = (
        ('M', '男性'),
        ('F', '女性'),
    )
    gender = models.CharField(max_length=2, choices=choices, default='M')


# 通过上述代码，我们定义了一个名叫 Book 的数据表。
# 数据表由以下字段构成书名（title）、出版社（public）、价格（price）、零售价（retail_price），
# 而且对每个字段都做添加了相应的字段属性以及字段选项。
