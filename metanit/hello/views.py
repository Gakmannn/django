from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseNotFound, JsonResponse
from .forms import UserForm
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

mySite = {
    '/html': {
        "header": "Hello Django", "message": "Welcome to Python", "langs": ["Python", "JavaScript", "Java", "C#", "C++"],
        "htmlIf":"<p>Число положительное</p>", "htmlElIf":"<p>Число отрицательное</p>", "htmlElse":"<p>Число равно нулю</p>", 
        "user": {
            "name":'test',
            "age": -32
        },
        "name":"Tom1", 'age':39, "isEnabled":None, "my_date":datetime.datetime(datetime.datetime.now().year,1,1) + datetime.timedelta(days=256)
    }
}
 
def index1(request):
    n = request.GET.get("n")
    if n:
        n = int(n)
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "index.html", context={**mySite[request.path], "n":n})

def contacts(request):
    userform = UserForm()
    return render(request, "contacts.html", {"form": userform})

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

# POST

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    userform = UserForm(request.POST)
    if userform.is_valid():
        name = userform.cleaned_data["name"]
        age = request.POST.get("age", 1)
        combo = request.POST.get("combo", '')
        langs = request.POST.getlist("languages", ["python"])
        return HttpResponse(f"""
                    <div>Name: {name}  Age: {age}<div>
                    <div>Languages: {langs}</div>
                    <div>Combo: {combo}</div>
                """)
    else:
        return HttpResponse("Invalid data")