from django.shortcuts import render, HttpResponse

# Create your views here.
import datetime

def index(request): #　request类似于ｓｅｌｆ
    name_dict = {
        'jky':[28,'IT','M'],
        'jack':[21,'IT','F'],
        'fugui':[28,'网络营销','M']
    }
    # html = "<h1>Hello World!</h1>"
    # f = open('templates/index.html')
    # return HttpResponse(f.read())
    return render(request, 'index.html', {'names':name_dict}) # 渲染页面，必须要去settings下设置

def show_date(request):
    c_date = datetime.datetime.now()
    html = '''<h1>你好啊帥! 当前时间为:
            <span style='color:red'> %s</span></h1>''' % c_date
    return HttpResponse(html)

def show_date_plus(request, num):
    print(num,"=================")
    c_date = datetime.datetime.now() + datetime.timedelta(days=int(num))
    html = '''<h1>你好啊帥! 当前时间为:
                <span style='color:red'> %s</span></h1>''' % c_date
    return HttpResponse(html)

def year_archive(request, year): # 这里的year就不能改成其他的变量了，因为在控制器中已经声明好了
    print('-------------',year)
    return HttpResponse(year)

def month_archive(request, year, month, name):
    print("============", year, month, name)
    return HttpResponse(year+" "+month)

def haohua(request):
    print('haohua')
    return HttpResponse("豪华车哟")


