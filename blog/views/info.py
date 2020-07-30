from django.shortcuts import render
from django.views.generic import View
from blog.models import Article,Sort
import markdown

class Articles(View):
    # model = Article
    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset=queryset)
    #     print(1,obj)
    #     obj.update_number()
    #     return obj

    def get(self, request ,id,*args, **kwargs):

        article = Article.objects.filter(id=id).first()
        article.number += 1
        article.save()

        article.content = markdown.markdown(article.content.replace("\r\n", '  \n'),extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ],safe_mode = True,enable_attributes = False)
        context = {'article':article}

        clafy_obj = Sort.objects.values('id', 'name').order_by('id')
        # clafy_obj = {'clafy_obj':sort_obj}
        # print(clafy_obj)
        # print(sort_obj)
        return render(request,'info.html',locals())
        # return render(request,'info.html',context,{'clafy_obj':sort_obj})