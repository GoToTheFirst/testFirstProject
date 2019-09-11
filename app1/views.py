from django.shortcuts import render,HttpResponse

# Create your views here.
from .models import Student

def insert(request):
    #Student.objects.create(name="gzci")
    #Student.objects.create(age="18")
    for i in range(100):
        if i%3==0:
            sexValue = False
        else:
            sexValue = True
        stu = Student(name="gzc"+str(i),age=i,sex=sexValue)
        stu.save()
    return HttpResponse("这是测试！")
def dropAll(request):
    Student.objects.all().delete()
    return HttpResponse("删除集合里面的全部内容")
def querry(request):
    a = list(Student.objects.all())
    for i in a:
        print(i.name)
    return HttpResponse("查询所有并输出数据")
"""
stu = Student.objects.filter(name="gzc1")
    #print(stu.size())
    #stu = Student.objects.get(name="gzc1")
    stu[0].name = "谷争昌"
    stu[0].save()
    print(stu[0].name)
    print("修改数据")
"""
def gai(request):
    Student.objects.filter(name="gzc1")[0].update(name="谷争昌")
    return HttpResponse("查询修改数据")