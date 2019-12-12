from django.shortcuts import render
from django.views import View

from info.models import *
from django.http import HttpResponse,JsonResponse
from django.http import JsonResponse
import json
from .models import EmployeeInfo

# from django.core.serializers import serialize

# json_data = serialize('json', goods) # str
# json_data = json.loads(json_data) # 序列化成json对象
def index(request):
    pass

def assessmonthinfo(request):
    einfo = EmployeeInfo.objects.get(id=1)
    return JsonResponse({'data': einfo.month})


# 录入部门考核成绩
def assessinfo(request):
    tableData = json.loads(request.body)
    einfo = EmployeeInfo.objects.get(id=1)
    # print(tableData)
    for i in tableData["tableData"]:
        # print(i)
        if i["dafen"] == "":
            return JsonResponse({"num": "2", "message": "填写不完整"})
        else:
            try:
                db = Assess.objects.get(name=i["bumen"],month = int(i["time"]))
            except:
                db = Assess()
            db.name = i["bumen"]
            db.month = int(i["time"])
            db.points = i["dafen"]
            lastinfo = EmployeeInfo.objects.filter(department=i["bumen"],month = int(i["time"]))[0]
            db.departmentclass = lastinfo.lastinfo
            db.save()
    # r = ['2I业务营销中心', '党政综合管理部', '连锁渠道营销中心', '订单运营中心', '互联网服务体验中心', '互联网合作平台营销中心', '互联网流量运营中心', '互联网系统运营中心', '商城营销中心',
    #      '经营监控中心', '数据分析应用中心', '资源支撑运营中心']
    Ds1 = Assess.objects.filter(name__in=['2I业务营销中心', '连锁渠道营销中心', '互联网合作平台营销中心', '商城营销中心'], month=einfo.month).order_by(
        '-points')
    Ds2 = Assess.objects.filter(
        name__in=['订单运营中心', '互联网服务体验中心', '互联网流量运营中心', '互联网系统运营中心', '经营监控中心', '数据分析应用中心', '资源支撑运营中心'], month=einfo.month).order_by('-points')
    Ds3 = Assess.objects.filter(name__in=['党政综合管理部'], month=einfo.month).order_by('-points')
    rank1 = 1
    rank2 = 1
    rank3 = 1
    for i in Ds1:
        i.rank = rank1
        i.save()
        rank1 += 1
    for i in Ds2:
        i.rank = rank2
        i.save()
        rank2 += 1
    for i in Ds3:
        i.rank = rank3
        i.save()
        rank3 += 1
    return JsonResponse({"num": "1", "message": "验证成功"})

def assessdatainfo(request):
    db = Assess.objects.all()
    result = []  # 构造一个空列表
    for i in db:
        result.append({  # 构造需要的数据  全部放入result中.
            'bumen': i.name,
            'time': '%d' % i.month,
            # 'marks': '%d' %i.mgrade,
            'dafen': str(i.points)
        })
    return JsonResponse({"status": 0, 'data': result})


# 考勤录入
def attenceinfo(request):
    data = json.loads(request.body)["formdata"]
    name = data.get("name")
    time = data.get("time")
    if name is not None and time is not None:
        db = EmployeeInfo.objects.get(name=name)
        if db.month == int(time):
            db.attendance = True
            db.save()
            return JsonResponse({"num": "1", "message": "表格建立成功"})
        else:
            return JsonResponse({"error": "time is None"})
    else:
        return JsonResponse({"error": "name is None"})
    # return JsonResponse({"messege": "成功录入"})


# 生成markinfo展示的表
def tableinfo(request):
    Employeedata = EmployeeInfo.objects.filter(attendance=0)
    print(Employeedata)
    for i in Employeedata:
        # 第一种方法
        # Markdata = MarkInfo.objects.create(name = i.name,jobnum = i.jobnum,department = i.department,mgrade = i.mgrade,month = i.month,lastinfo = i.lastinfo)
        # 第二种方法
        try:
            Markdata = MarkInfo.objects.get(jobnum=i.jobnum,month=i.month)
        except:
            Markdata = MarkInfo()
        Markdata.name = i.name
        Markdata.jobnum = i.jobnum
        Markdata.department = i.department
        Markdata.managerid = i.managerid
        Markdata.mgrade = i.mgrade
        Markdata.month = i.month
        Markdata.lastinfo = i.lastinfo
        Markdata.save()
    return JsonResponse({"num": "1","message": "表格建立成功"})

# 录入打分成绩
def managermarkinfo(request):
    tableData = json.loads(request.body)
    msg4 = int(tableData['msg4'])
    msg5 = int(tableData['msg5'])
    msg6 = int(tableData['msg6'])
    msg7 = int(tableData['msg7'])
    for i in tableData["tableData"]:
        db = MarkInfo.objects.get(name=i["name"],month=int(i["time"]),jobnum = i["jobnum"])
        le = i["level"]
        if le == "":
            return JsonResponse({"num": "3", "message": "验证失败"})
        else:
            # print(df)
            db.level = le
            db.save()
    # 对评级的个数的校验
    leveldata = MarkInfo.objects.filter(department=i["department"],month=int(i["time"]))
    levellist = []
    # gradelist = []
    for i in leveldata:
        levellist.append(i.level)
        # gradelist.append(i.mgrade)
    num1 = str(levellist).count("A")
    num2 = str(levellist).count("B+")
    num3 = str(levellist).count("B") - num2
    num4 = str(levellist).count("C")
    num5 = str(levellist).count("D")
    num6 = len(levellist)
    if msg4 == num1 and msg5 == num2 and msg6 == (num3 + num4 + num5) and msg7 <= (num4 + num5):
        print(num1 + num2)
        MarkInfo.objects.filter(level='A').update(jifen=100)
        MarkInfo.objects.filter(level='B+').update(jifen=90)
        MarkInfo.objects.filter(level='B').update(jifen=80)
        MarkInfo.objects.filter(level='C').update(jifen=70)
        MarkInfo.objects.filter(level='D').update(jifen=60)
        j = MarkInfo.objects.filter()
        return JsonResponse({"num": "1", "message": "验证成功"})
    else:
        return JsonResponse({"num": "2", "message": "验证失败"})



def marknameinfo(request):     #渲染不同经理打分页面的员工数据
    last_info = request.user.last_name
    einfo = EmployeeInfo.objects.get(id=1)
    if MarkInfo.objects.filter(lastinfo=last_info,month=einfo.month).exists():
        db = MarkInfo.objects.filter(lastinfo=last_info,month=einfo.month)
    else:
        return JsonResponse({"status": 0, 'num': "1"})
    result = []   # 构造一个空列表
    for i in db:
        result.append({   # 构造需要的数据  全部放入result中.
            'jobnum': i.jobnum,
            'department': i.department,
            'name': i.name,
            'time': i.month,
            'dafen': i.mgrade,
            'level': i.level
        })
    return JsonResponse({"status": 0, 'data': result})  # return data

def managermarkdatainfo(request):#传送不同经理的全量打分数据
    last_info = request.user.last_name
    db = MarkInfo.objects.filter(lastinfo=last_info)
    result = []  # 构造一个空列表
    for i in db:
        if i.jifen == None:
            result.append({  # 构造需要的数据  全部放入result中.
                'jobnum': i.jobnum,
                'name': i.name,
                'department': i.department,
                'month': '%d' % i.month,
                # 'marks': '%d' %i.mgrade,
                'level': '未录入',
                'jifen': '未录入'
            })
        else:
            result.append({  # 构造需要的数据  全部放入result中.
                'jobnum': i.jobnum,
                'name': i.name,
                'department': i.department,
                'month': '%d' % i.month,
                # 'marks': '%d' %i.mgrade,
                'level': i.level,
                'jifen': '%d' % i.jifen
            })
    # for i in db:
    #     result.append({  # 构造需要的数据  全部放入result中.
    #         'jobnum': i.jobnum,
    #         'name': i.name,
    #         'department': i.department,
    #         'month': '%d' % i.month,
    #         # 'marks': '%d' % i.mgrade,
    #         'level': i.level,
    #         'jifen': '%d' % i.jifen
    #     })
    return JsonResponse({"status": 0, 'data': result})

def downloadinfo(request):#传送全量的打分数据
    db = MarkInfo.objects.all()
    db2 = EmployeeInfo.objects.filter(attendance=1)
    result = []   # 构造一个空列表
    for i in db:
        if i.jifen == None:
            result.append({  # 构造需要的数据  全部放入result中.
                'jobnum': i.jobnum,
                'name': i.name,
                'department': i.department,
                'month': '%d' % i.month,
                # 'marks': '%d' %i.mgrade,
                'level': '未录入',
                'jifen': '未录入'
            })
        else:
            result.append({  # 构造需要的数据  全部放入result中.
                'jobnum': i.jobnum,
                'name': i.name,
                'department': i.department,
                'month': '%d' % i.month,
                # 'marks': '%d' %i.mgrade,
                'level': i.level,
                'jifen': '%d' % i.jifen
            })
    # for i in db:
    #     result.append({  # 构造需要的数据  全部放入result中.
    #         'jobnum': i.jobnum,
    #         'name': i.name,
    #         'department': i.department,
    #         'month': '%d' % i.month,
    #         'marks': '0',
    #         'level': '0',
    #         'jifen': '0'
    #     })

    return JsonResponse({"status": 0, 'data': result})

def manageruseropeninfo(request):#打开经理打分账号登录权限
    date = Department.objects.get(id = 1)
    lastdate = json.loads(request.body)
    lastdate1 = int(lastdate['lastdate'])
    date.month = lastdate1
    if date.month == 31:
        date.save()
        return JsonResponse({"status": 0, 'num': "1"})
    else:
        return JsonResponse({"status": 0, 'num': "0"})

def kpiuseropeninfo(request):#打开kpi录入账号登录权限
    date = Department.objects.get(id = 1)
    lastdate = json.loads(request.body)
    lastdate1 = int(lastdate['lastdate'])
    date.grade = lastdate1
    if date.grade == 31:
        date.save()
        return JsonResponse({"status": 0, 'num': "1"})
    else:
        return JsonResponse({"status": 0, 'num': "0"})

def manageruserresetinfo(request):#重置经理打分登陆权限
    date = Department.objects.get(id=1)
    lastdate = json.loads(request.body)
    lastdate1 = int(lastdate['lastdate2'])
    date.month = lastdate1
    if date.month == 27:
        date.save()
        return JsonResponse({"status": 0, 'num': "1"})
    else:
        return JsonResponse({"status": 0, 'num': "0"})

def kpiuserresetinfo(request):
    date = Department.objects.get(id=1)
    lastdate = json.loads(request.body)
    lastdate1 = int(lastdate['lastdate1'])
    date.grade = lastdate1
    if date.grade == 20:
        date.save()
        return JsonResponse({"status": 0, 'num': "1"})
    else:
        return JsonResponse({"status": 0, 'num': "0"})

def manageropenreceiveinfo(request):#经理打分账号获取账号登录截至时间
    date = Department.objects.get(id=1)
    lastdate = date.month
    return JsonResponse({'num':0,'data':lastdate})

def kpiopenreceiveinfo(request):#经理打分账号获取账号登录截至时间
    date = Department.objects.get(id=1)
    lastdate = date.grade
    return JsonResponse({'num':0,'data':lastdate})


def computeinfo(request):
    last_info = request.user.last_name
    einfo = EmployeeInfo.objects.get(id=1)

    if  Assess.objects.filter(month=einfo.month).exists():
        departmentdata = Assess.objects.get(departmentclass=last_info, month=einfo.month)
        Ds1 = Assess.objects.get(name__in=['2I业务营销中心', '连锁渠道营销中心', '互联网合作平台营销中心', '商城营销中心'], month=einfo.month,rank=4).points
        Ds2 = Assess.objects.get(name__in=['订单运营中心', '互联网服务体验中心', '互联网流量运营中心', '互联网系统运营中心', '经营监控中心', '数据分析应用中心', '资源支撑运营中心'],month=einfo.month, rank=7).points
        Ds3 = Assess.objects.get(name='党政综合管理部', month=einfo.month).points
    else:
        return JsonResponse({"status": 0, 'num': "0"})
    person = MarkInfo.objects.filter(lastinfo=last_info,month=einfo.month)
    # 需要先考勤录入才能执行
    count_of_department = len(person)
    print(count_of_department)
    rr = {}
        # rr['department'] = p
    # if departmentdata.points is None:
    #     return JsonResponse({"status": 0, 'num': "0"})

    if departmentdata.points >= 100:
            # rr = {'name': 'depart' + str(d + 1)}
        rr['A'] = round(count_of_department * 0.3 + 0.01)
        rr['B+'] = round(count_of_department * (0.2 + 0.3) + 0.01) - rr['A']
        rr['B+C+D'] = count_of_department - round(count_of_department * (0.2 + 0.3) + 0.01)
        rr['C+D'] = 0
        print('您部门本月有%f个A，%f个B+，%f个B、C、D，其中%f个C、D' % (rr['A'], rr['B+'], rr['B+C+D'], rr['C+D']))
    elif departmentdata.points < 100 and departmentdata.points >= 90:
            # rr = {'name': 'depart' + str(d + 1)}
        rr['A'] = round(count_of_department * 0.2 + 0.01)
        rr['B+'] = round(count_of_department * (0.2 + 0.2) + 0.01) - rr['A']
        rr['B+C+D'] = count_of_department - round(count_of_department * (0.2 + 0.2) + 0.01)
        rr['C+D'] = 0
        print('您部门本月有%f个A，%f个B+，%f个B、C、D，其中%f个C、D' % (rr['A'], rr['B+'], rr['B+C+D'],rr['C+D']))
    elif departmentdata.points < 90 and departmentdata.points >= 80 and (departmentdata.points == Ds1 or departmentdata.points == Ds2 or departmentdata.points == Ds3):
        rr['A'] = round(count_of_department * 0.2 + 0.01)
        rr['B+'] = round(count_of_department * (0.15+0.2) + 0.01) - rr['A']
        rr['B+C+D'] = count_of_department - round(count_of_department * (0.15 + 0.2) + 0.01)
        rr['C+D'] = round(count_of_department * 0.05)
        if rr['C+D'] < 1:
            rr['C+D'] = 1
        print('您部门本月有%f个A，%f个B+，%f个B、C、D，其中C、D为%f' % (rr['A'], rr['B+'], rr['B+C+D'], rr['C+D']))
    # elif departmentdata.points < 90 and departmentdata.points == Ds3 and departmentdata.ramk ==1:



    elif departmentdata.points < 90 and departmentdata.points >= 80 and departmentdata.points != Ds1 and departmentdata.points != Ds2 and departmentdata.points != Ds3:
        rr['A'] = round(count_of_department * 0.2 + 0.01)
        rr['B+'] = round(count_of_department * (0.15 + 0.2) + 0.01) - rr['A']
        rr['B+C+D'] = count_of_department - round(count_of_department * (0.15 + 0.2) + 0.01)
        rr['C+D'] = 0
        print('您部门本月有%f个A，%f个B+，%f个B、C、D，其中%f个C、D' % (rr['A'], rr['B+'], rr['B+C+D'], rr['C+D']))
    elif departmentdata.points < 80 and (departmentdata.points == Ds1 or departmentdata.points == Ds2 or departmentdata.points == Ds3):
        rr['A'] = round(count_of_department * 0.2 + 0.01)
        rr['B+'] = round(count_of_department * (0.15 + 0.2) + 0.01) - rr['A']
        rr['B+C+D'] = count_of_department - round(count_of_department * (0.15 + 0.2) + 0.01)
        rr['C+D'] = round(count_of_department * 0.1 + 0.01)
        if rr['C+D'] < 1:
            rr['C+D'] = 1
        print('您部门本月有%f个A，%f个B+，%f个B、C、D，其中%f个C、D' % (rr['A'], rr['B+'], rr['B+C+D'], rr['C+D']))
    elif departmentdata.points < 80 and departmentdata.points != Ds1 and departmentdata.points != Ds2 and departmentdata.points != Ds3:
        rr['A'] = round(count_of_department * 0.2 + 0.01)
        rr['B+'] = round(count_of_department * (0.15 + 0.2) + 0.01) - rr['A']
        rr['B+C+D'] = count_of_department - round(count_of_department * (0.15 + 0.2) + 0.01)
        rr['C+D'] = 0
        print('您部门本月有%f个A，%f个B+，%f个B、C、D，其中%f个C、D' % (rr['A'], rr['B+'], rr['B+C+D'], rr['C+D']))
    rr['kpi'] = departmentdata.points
    rr['rank'] = departmentdata.rank
    rr['person'] = count_of_department
    return JsonResponse({"status": 0, 'data': rr})