from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseNotFound, JsonResponse
import datetime

# Create your views here.

arr = [1,2,3]
 
links = '''
    <nav>
    <a href="/">Главная</a> |
    <a href="/1">1</a> |
    <a href="/2">2</a>
    </nav>
'''
 
def index(request):
    admin = request.GET.get("admin")
    if (admin):
        response = HttpResponse("Hello " + admin)
        response.set_cookie("username", admin)
        return response
    return HttpResponse(links+"Hello " + str(datetime.datetime.now()) + " METANIT.COM " + str(arr[1]) + ' ' + str(request.COOKIES))

def json(request):
    return JsonResponse({"name": "Tom", "age": 38})

def i1(request):
    if (request.path.endswith('/')):
        return HttpResponsePermanentRedirect(request.path[:-1])
    return HttpResponse(links+"<h1>Hello 1 METANIT.COM</h1>")

def i2(request):
    if (request.path.endswith('/')):
        return HttpResponsePermanentRedirect(request.path[:-1])
    name = request.path.split('/')[2]
    if (len(request.path.split('/'))>3):
        return HttpResponseNotFound()
    return HttpResponse(links+"<h1>Hello "+ name +"</h1>")

def i22(request, slug):
    if (request.path.endswith('/')):
        return HttpResponsePermanentRedirect(request.path[:-1])
    # name = request.path.split('/')[2]
    # if (len(request.path.split('/'))>3):
    #     return HttpResponseNotFound()
    return HttpResponse(links+"<h1>Hello "+ slug +"</h1>")

def products(request):
    return HttpResponse(links+"Список товаров")
 
def new(request):
    return HttpResponse(links+"Новые товары")
 
def top(request):
    return HttpResponse(links+"Наиболее популярные товары")