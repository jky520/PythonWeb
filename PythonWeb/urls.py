"""PythonWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# 这是总控制器

from django.conf.urls import url
from django.contrib import admin

from app01 import views #, urls # 导入app01下的views和urls

active = {'menu':'active'} # 自定义的全局变量

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 子项目路劲的配置
    # url(r'^second_hand/', include(urls),),  # 把所有以second_hand开头的请求路径全部放到app01下的urls中
    # 同时还要去app01下的子项目创建urls
    # 配置路由，也就是控制器
    # url(r'^$', views.index, name='dashboard'), # 在view里用index方法处理
    url(r'^$', views.home, name='dashboard'), # 在view里用home方法处理
    url(r'^user_index/$', views.user_index, name='user_index'),
    url(r'^assert_index/$', views.assert_index, name='assert_index'),
    # url(r'^show_date/$', views.show_date),
    # url(r'^show_date/(\d{2})/$', views.show_date_plus),

    # url(r'^articles/2003/$', views.special_case_2003),
    # url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    # url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive), # 相当于视图中的关键参数名
    # url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.day_archive),
    # url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, {'name':'jky'}), # {'name':'jky'}相当于java的默认参数
]
