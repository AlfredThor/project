from django.shortcuts import render
from django.views.generic import View
from blog.models import Sort,Article
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

class Clafy(View):

    def get(self,request,aid):
        article_obj = Article.objects.filter(sort=aid).values('id','title','intro','user__username','sort__name','time','number').order_by('id')

        currentPage = int(request.GET.get('page', 1))
        paginator = Paginator(article_obj, 15)

        if paginator.num_pages > 11:
            if currentPage - 5 < 1:
                pageRange = range(1, 11)
            elif currentPage + 5 > paginator.num_pages:
                pageRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
            else:
                pageRange = range(currentPage - 5, currentPage + 5)
        else:
            pageRange = paginator.page_range
        try:
            topic_obj = paginator.page(currentPage)
        except PageNotAnInteger:
            topic_obj = paginator.page(1)
        except EmptyPage:
            topic_obj = paginator.page(1)

        clafy_obj = Sort.objects.values('id', 'name').order_by('id')

        return render(request,'clafy.html',locals())