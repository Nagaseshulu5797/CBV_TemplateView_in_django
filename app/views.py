from typing import Any, Dict
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse
class cbv_data(TemplateView):
    template_name='cbv_data.html'
    def get_context_data(self, **kwargs):
        EDCO=super().get_context_data(**kwargs)
        EDCO['name']='Seshulu'
        EDCO['age']=21
        return EDCO
    
class cbv_form(TemplateView):
    template_name='cbv_form.html'
    def get_context_data(self, **kwargs):
        CO=super().get_context_data(**kwargs)
        SO=StudentForm()
        CO['SO']=SO
        return CO
    
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data is inserted')
    
    
