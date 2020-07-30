from django.shortcuts import render
from django.views.generic import View
from blog.models import Article

class Share(View):

    def get(self,request):

        article_obj_python = Article.objects.filter(sort=1).values('id','title').order_by('id')[:10]
        article_obj_django = Article.objects.filter(sort=2).values('id','title').order_by('id')[:10]
        article_obj_mysql = Article.objects.filter(sort=3).values('id','title').order_by('id')[:10]
        article_obj_redis = Article.objects.filter(sort=4).values('id','title').order_by('id')[:10]
        article_obj_linux = Article.objects.filter(sort=5).values('id','title').order_by('id')[:10]
        article_obj_docker = Article.objects.filter(sort=6).values('id','title').order_by('id')[:10]

        return render(request,'share.html',{'article_obj_python':article_obj_python,'article_obj_django':article_obj_django,
                                            'article_obj_mysql':article_obj_mysql,'article_obj_redis':article_obj_redis,
                                            'article_obj_linux':article_obj_linux,'article_obj_docker':article_obj_docker})