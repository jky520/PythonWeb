#_*_coding:utf-8_*_
# 自己新增的控制器（复制过来改即可）
from django.conf.urls import url

urlpatterns = [
    url(r'haohua/$', view='haohua'), # 值得注意的是：在上一级项目中已经加上了^,所以这里url的r''里只要写second_hand下一层路径即可,如：r'haohua'什么的
]
