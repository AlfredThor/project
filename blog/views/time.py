from django.shortcuts import render
from django.views.generic import View
from blog.models import Article,Sort
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage

class Time(View):

    def get(self,request):

        article_obj = Article.objects.values('id','title','time',).order_by('-time')

        currentPage = int(request.GET.get('page', 1))
        paginator = Paginator(article_obj, 20)

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
            article_obj = paginator.page(currentPage)
        except PageNotAnInteger:
            article_obj = paginator.page(1)
        except EmptyPage:
            article_obj = paginator.page(1)

        return render(request,'time.html',locals())