# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import pymysql
import json
import requests

# Create your views here.


def index(request):

    return render(request, 'showcase/index.html')


def notfound(request):

    return render(request, 'showcase/404.html')


def form_builder(request):

    return render(request, 'showcase/form_builder.html')


def base(request):

    return render(request, 'showcase/base.html')


def layouts(request):

    return render(request, 'showcase/layouts.html')


def API_MASTER(request):

    return render(request, 'showcase/API_MASTER.html')


def showcase(request):
    """
    从数据库中读取作者的用例信息，并用于前台可视化展示
    :param request:
    :return:
    """
    # 注意修改此处mysql服务的ip
    db = pymysql.connect("localhost", "root", "guchen", "guchen_test", charset='utf8')
    cursor = db.cursor()
    sql = "select * from userCaseInfo"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results
    # 向js中传递数据必须json.dumps()处理
    return render(request, "showcase/showcase.html", {'caseInfo': json.dumps(list(results))})


def apitest(request):

    request_method = request.GET['request_method']
    api_url = request.GET['api_url']
    print request_method
    print api_url
    r = requests.get(api_url)
    print r.content
    return render(request, 'showcase/API_MASTER.html',{'response': r.content})

def ytoAutoCaseCount(request):
    db = pymysql.connect("192.168.207.160", "root", "123qwe!@#", "autotest", charset='utf8')
    cursor = db.cursor()
    advertisementCount = "select total,succ,fail,percent from advertisement ORDER BY id DESC limit 1"
    membercenterCount = "select total,succ,fail,percent from membercenter ORDER BY id DESC limit 1"
    permissionCount = "select total,succ,fail,percent from permission ORDER BY id DESC LIMIT 1"
    saasCount = "select total,succ,fail,percent from saas ORDER BY id DESC LIMIT 1"
    cursor.execute(advertisementCount)
    advertisement_results = cursor.fetchall()
    cursor.execute(membercenterCount)
    membercenter_results = cursor.fetchall()
    cursor.execute(permissionCount)
    permission_results = cursor.fetchall()
    cursor.execute(saasCount)
    saas_results = cursor.fetchall()

    advertisement_results_list=list(advertisement_results[0])
    advertisement_results_list.append('advertisement')
    membercenter_results_list=list(membercenter_results[0])
    membercenter_results_list.append('membercenter')
    permission_results_list=list(permission_results[0])
    permission_results_list.append('permission')
    saas_results_list=list(saas_results[0])
    saas_results_list.append('saas')


    results = (advertisement_results_list,membercenter_results_list,permission_results_list,saas_results_list)
    # print results

    #获取用例总数
    advertisementNumSQL= 'select count(*) from advertisement'
    cursor.execute(advertisementNumSQL)
    advertisementNum = cursor.fetchall()

    membercenterNumSQL = 'select count(*) from membercenter'
    cursor.execute(membercenterNumSQL)
    membercenterNum = cursor.fetchall()

    permissionNumSQL = 'select count(*) from permission'
    cursor.execute(permissionNumSQL)
    permissionNum = cursor.fetchall()

    saasNumSQL = 'select count(*) from saas'
    cursor.execute(saasNumSQL)
    saasNum = cursor.fetchall()

    totalCount= int(results[0][0])+int(results[1][0])+int(results[2][0])+int(results[3][0])
    sucCount=int(results[0][1])+int(results[1][1])+int(results[2][1])+int(results[3][1])
    passRate=sucCount/float(totalCount)
    passRate ="%.2f%%" % (passRate * 100)
    # print totalCount
    # print results
    # 向js中传递数据必须json.dumps()处理
    return render(request, "showcase/ytoAutoCaseCount.html", {'caseInfo': json.dumps(list(results)),
                                                              'totalCount':totalCount,
                                                              'sucCount':sucCount,
                                                              'passRate':passRate})

# ytoAutoCaseCount()


def addProject(request):
    '''
    新增自动化测试项目
    :param request:
    :return:
    '''
    # db = pymysql.connect("192.168.207.160", "root", "123qwe!@#", "autotest", charset='utf8')
    db = pymysql.connect("localhost", "root", "guchen", "guchen_test", charset='utf8')
    cursor = db.cursor()
    if request.method == "POST":
        projectName = request.POST.get("tableName", None)
        comment = request.POST.get("tableComment", None)
        print projectName, comment
        addProjectSQL = (
            "CREATE TABLE `%s` ("
            "`id` int(32) NOT NULL AUTO_INCREMENT,"
            " `total` varchar(64) DEFAULT NULL,"
            "`succ` varchar(64) DEFAULT NULL,"
            " `fail` varchar(64) DEFAULT NULL,"
            "`percent` varchar(64) DEFAULT NULL,"
            "`author` varchar(64) DEFAULT NULL,"
            " `add_time` datetime DEFAULT CURRENT_TIMESTAMP,"
            " PRIMARY KEY (`id`))"
            "ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='%s'"
            % (projectName, comment)
        )
        cursor.execute(addProjectSQL)
        cursor.close()
    status = 'success'
    return render(request,"showcase/projectList.html",{'status':json.dumps(status)})

def projectList(requset):

    return render(requset,"showcase/projectList.html")

def bootstrapTable(request):
    db = pymysql.connect("192.168.207.160", "root", "123qwe!@#", "autotest", charset='utf8')
    cursor = db.cursor()
    datalist = []
    saasCount = "select total,succ,fail,percent from saas ORDER BY id DESC LIMIT 1"
    cursor.execute(saasCount)
    saas_results = cursor.fetchall()
    # print list(saas_results[0])
    # datalist.append(list(saas_results[0]))
#     字典js接收不到
    datalist= {
    	"total": 3,
    	"rows": [{
    		"id": 1,
    		"name": "mdm",
    		"price": 200
    	}]
    }
#     datalist= [{
#     		"id": 1,
#     		"name": "mdm",
#     		"price": 200
#     	}]
    # print datalist
    # 列表js可以接收
    # datalist=[['主数据','t_mdm', '200'],['客户管家','t_khm', '30']]
    dl=json.dumps(datalist)
    return render(request, 'showcase/bootstrapTable.html', {'datalist': dl})



def getdata(request):
    db = pymysql.connect("192.168.207.160", "root", "123qwe!@#", "autotest", charset='utf8')
    cursor = db.cursor()
    rows = []
    count="select COUNT(*) from saas"
    saasCount = "select id,total,succ,fail,percent from saas ORDER BY id DESC"
    cursor.execute(count)
    count = cursor.fetchone()
    cursor.execute(saasCount)

    saas_results = cursor.fetchall()
    print list(saas_results)
    for i in list(saas_results):
        print i
        rows.append({"id": i[0], "name": i[1], "price": i[4]})
    print rows
    datalist={
        "total": count[0],
        "rows": rows
    }

    print datalist
    # rows返回为json数组
    return HttpResponse(json.dumps(rows))
    # datalist为json对象
    # reqturn HttpResponse(json.dumps(datalist))