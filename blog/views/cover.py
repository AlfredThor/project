from django.shortcuts import render
from django.views.generic import View
from blog.models import Article,Sort

class Cover(View):

    def get(self,request):

        article_obj = Article.objects.values('id', 'title', 'intro', 'user__username', 'sort__name', 'time',
                                             'number').order_by('-number')[:10]

        clafy_obj = Sort.objects.values('id', 'name').order_by('id')

        return render(request,'fengmian.html',locals())