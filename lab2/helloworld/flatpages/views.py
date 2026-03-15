# #coding:utf-8
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse(u'Привет, Мир!')

#coding:utf-8
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def static_handler(request):
    return render(request, 'static_handler.html', {})