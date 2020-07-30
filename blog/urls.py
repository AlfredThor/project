from  django.urls import re_path
from blog.views.about import About
from blog.views.cover import Cover
from blog.views.enroll import Enroll
from blog.views.index import Index
from blog.views.info import Articles
from blog.views.list import List
from blog.views.share import Share
from blog.views.time import Time
from blog.views.logins import Logins
from blog.views.clafy import Clafy

urlpatterns = [
    # 主页
    re_path(r'^index/$', Index.as_view(), name='index/'),
    # fenlei
    re_path(r'^clafy/(?P<aid>\d+)/$', Clafy.as_view(), name='clafy/'),
    # 封面
    re_path(r'^cover/$', Cover.as_view(), name='cover/'),
    # 关于我
    re_path(r'^about/$', About.as_view(), name='about/'),
    # 文章详情
    re_path(r'^article/(?P<id>\d+)/$', Articles.as_view(), name='article/'),
    # 博客分类
    re_path(r'^list/$', List.as_view(), name='list/'),
    # 知识库
    re_path(r'^share/$', Share.as_view(), name='share/'),
    # 时光轴
    re_path(r'^time/$', Time.as_view(), name='time/'),

    # 搜索
    # re_path(r'^hunt/$', hunt.as_view(), name='hunt/'),
    # 注册
    re_path(r'^enroll/$', Enroll.as_view(), name='enroll/'),
    # 登录
    re_path(r'^login/$', Logins.as_view(), name='login/'),
]