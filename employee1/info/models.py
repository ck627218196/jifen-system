from django.db import models
from django.db.models import *
# from django.contrib.auth.models import AbstractUser

# class MyUser(AbstractUser):
#     username = models.CharField(max_length=32,unique=True)
#     password = models.CharField(max_length=64)
#
#     def __str__(self):
#         return self.username


# Create your models here.
class Assess(Model):
    name = CharField(verbose_name='部门名',max_length=50)
    month = IntegerField(verbose_name='考核月份',default = 0)
    points = FloatField(verbose_name='考核分数',null=True)
    departmentclass = CharField(verbose_name='部门分类', max_length=40)
    rank = IntegerField(verbose_name='部门考核排名',null=True)
class Department(Model):
    name = CharField(verbose_name='部门名', max_length=50)
    month = IntegerField(verbose_name='考核月份', default=0)
    grade = IntegerField(verbose_name='部门得分', default=0) #打分
    managerid = CharField(verbose_name='部门经理', max_length=40)
class EmployeeInfo(Model):
    name = CharField(verbose_name='员工姓名', max_length=40)
    jobnum = CharField(verbose_name='员工ID', max_length=40)
    department = CharField(verbose_name='员工所属部门', max_length=50,null = True)
    managerid = CharField(verbose_name='部门经理',null=True, max_length=40)
    attendance = BooleanField(verbose_name="是否出勤", default=False)
    mgrade = IntegerField(verbose_name='经理打分', null=True) # 打分
    month = IntegerField(verbose_name='考核月份', null=True, default=0)
    # 这里我建议加一个字段 用来映射last_name
    lastinfo = IntegerField(verbose_name="对应渲染用户", null=True, default=0)

class MarkInfo(Model):
    name = CharField(verbose_name='员工姓名', max_length=40)
    jobnum = CharField(verbose_name='员工ID', max_length=40)
    department = CharField(verbose_name='员工所属部门', max_length=50,null = True)
    level = CharField(verbose_name='评级',null=True, max_length=40)
    jifen = IntegerField(verbose_name='积分', null=True)
    mgrade = IntegerField(verbose_name='经理打分', null=True) # 打分
    month = IntegerField(verbose_name='考核月份', null=True, default=0)
    # 这里我建议加一个字段 用来映射last_name
    lastinfo = IntegerField(verbose_name="对应渲染用户", null=True, default=0)
class Others(Model):
    name = CharField(verbose_name='名称', max_length=40)
    age = IntegerField(verbose_name='年龄', null=True)
    info = IntegerField(verbose_name="信息", null=True, default=0)
    number = IntegerField(verbose_name='数字', null=True)



# class Group(Model):
#     name = CharField(verbose_name='员工姓名',max_length=50)
#     department = CharField(verbose_name='部门名',max_length=50)
#     group =  CharField(verbose_name = '化小团队', null =True,max_length=50)

# class EmployeeExamine(Model):
#     info = OneToOneField(EmployeeInfo,)
#     name = CharField(verbose_name='员工姓名',max_length=40)
#     grade = IntegerField(verbose_name='员工打分',default = 0) #打分
#     # department = CharField(verbose_name='员工所属部门',default=0,null = True)
#     # group = CharField(verbose_name = '化小团队', null =True,max_length=50)
#

# class EmployeeAttentance(Model):
#     name = CharField(verbose_name='员工姓名',max_length=40)
#     jobnum = ForeignKey(EmployeeInfo,verbose_name='员工ID',on_delete = SET_NULL,null = True)
#     department = ForeignKey(Department,verbose_name='员工所属部门',on_delete = SET_NULL,null = True)
#     group = CharField(verbose_name = '化小团队', null =True,max_length=50)
#     managerid = CharField(verbose_name='部门经理',null=True,max_length=40)

# class Userid(Model):
#     name = CharField(verbose_name='姓名', max_length=40)
#     type = IntegerField(verbose_name='管理员类型', default=0)
#     department = ForeignKey(Department, verbose_name='所属部门', on_delete=SET_NULL, null=True)
#     group = CharField(verbose_name = '化小团队', null =True,max_length=50)

