from django.shortcuts import render
from django.views.generic import View

class Logins(View):

    def get(self,request):

        return render(request,'')