from django.contrib import admin
from django.db import models
from blog import models as blog_models
from mdeditor.widgets import MDEditorWidget

class ExampleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

admin.site.register(blog_models.Article,ExampleModelAdmin)

class SortAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(blog_models.Sort,SortAdmin)

class UseripAdmin(admin.ModelAdmin):
    list_display = ['id','ip','count','time']

admin.site.register(blog_models.Userip,UseripAdmin)

admin.site.register(blog_models.Member)