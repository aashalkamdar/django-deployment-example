from django.shortcuts import render
from django.urls import include,re_path
# Create your views here.
def index(request):
    context_dict = {'text':'hello world','number':'100'}
    return render(request,'basic_app/index.html',context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative_url_templates(request):
    return render(request,'basic_app/relative_url_templates.html')
