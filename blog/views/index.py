from django.shortcuts import render
from django.views.generic import View
from blog.models import Sort,Article

class Index(View):

    def get(self,request):

        sort_obj = Sort.objects.values('id','name').order_by('id')

        article_obj = Article.objects.values('id','title','intro','user__username','sort__name','time','number').order_by('-number')[:10]

        # currentPage = int(request.GET.get('page', 1))
        # paginator = Paginator(article_obj, 15)
        #
        # if paginator.num_pages > 11:
        #     if currentPage - 5 < 1:
        #         pageRange = range(1, 11)
        #     elif currentPage + 5 > paginator.num_pages:
        #         pageRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
        #     else:
        #         pageRange = range(currentPage - 5, currentPage + 5)
        # else:
        #     pageRange = paginator.page_range
        # try:
        #     article_obj = paginator.page(currentPage)
        # except PageNotAnInteger:
        #     article_obj = paginator.page(1)
        # except EmptyPage:
        #     article_obj = paginator.page(1)

        return render(request,'index.html',{'sort_obj':sort_obj,'article':article_obj})