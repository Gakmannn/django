from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseNotFound, JsonResponse, HttpResponseRedirect
from .forms import UserForm
import datetime
from django.db.models.query import RawQuerySet
from .models import Person, Product, Company, Course,Student,Enrollment
from django.db.models import Avg, Min, Max, Sum
import asyncio
  
# https://yourtodo.ru/posts/asinhronnyij-django  
  
async def get_person(id):
    person = await Person.objects.aget(id=id)
    print(person.name)
    return person

people = Person.objects.filter(age__lte=32).filter(age__gte=40)
print(people.query)
people = Person.objects.filter(age__lte=32) & Person.objects.filter(age__gte=40)
print(people.query)
people = Person.objects.filter(age__range=(32,40))
print(people.query)

people = Person.objects.filter(age__in=[32, 35, 38])
print(people.query)
people = Person.objects.filter(age=32) | Person.objects.filter(age=35) | Person.objects.filter(age=38)
print(people.query)
people = Person.objects.filter(name="Tom") ^ Person.objects.filter(age=22)
print(people.query)

people = Person.objects.filter(name__regex=r"(am|om)$").order_by("-name")
print(people.query)

# запускаем асинхронную функцию get_person
p = asyncio.run(get_person(3))
print(f"{p.id}.{p.name} - {p.age}")

# person = Person.objects.get(name="Tom") # Ошибка. Значений больше одного
# tom = Person.objects.create(name="Tom", age=23)
# tom = Person.objects.create(name="Tom", age=32)
# получаем все объекты
# people = Person.objects.bulk_create([
#     Person(name="Kate", age=24),
#     Person(name="Ann", age=21),
# ])

# Person.objects.get(id=2).delete()

# people = Person.objects.all().filter(name = "Tom").filter(age = 32)
people = Person.objects.all()
print(people.query)

 
# здесь происходит выполнения запроса в БД
for person in people:
    print(f"{person.id}.{person.name} - {person.age}")

# Create your views here.

toms = Person.objects.filter(name="Tom")
bobs = Person.objects.filter(name="Bob")
# объединяем два QuerySet
people = toms.union(bobs)
print(people.query)
print(people.values())

# получаем объект с самыми последними изменениями в поле id
latest_person = Person.objects.latest("id")
print(f"latest {latest_person.name} - {latest_person.age}")
 
# получаем объект c самыми ранними изменениями в поле name
earliest_person = Person.objects.earliest("id")
print(f"earliest {earliest_person.name} - {earliest_person.age}")

# получим первый объект
first_person = Person.objects.first()
print(f"{first_person.name} - {first_person.age}")

first_person1 = Person.objects.all()[:1]
print(f"{first_person1[0].name} - {first_person1[0].age}")
 
# получим последний объект
last_person = Person.objects.last()
print(f"{last_person.name} - {last_person.age}")
 
# получим первый объект из набора, отсортированного по возрасту
first_person = Person.objects.order_by("age").last()
print(f"{first_person.name} - {first_person.age}")

# средний возраст
avg_age = Person.objects.filter(name='Tom').aggregate(Avg("age"))
print(avg_age)
 
# минимальный возраст
min_age = Person.objects.aggregate(Min("age"))
print(min_age)
 
# максимальный возраст
max_age = Person.objects.aggregate(Max("age"))
print(max_age)
 
# сумма всех возрастов
sum = Person.objects.aggregate(Sum("age"))
print(sum)

raw = RawQuerySet("SELECT id, name FROM hello_person")


# создаем объект Company
# apple = Company.objects.create(name="Apple")
 
 
# # создание товара определенной компании
# apple.product_set.create(name="iPhone 8", price=67890)
 
# # отдельное создание объекта с последующим добавлением
# ipad = Product(name="iPad", price=34560)
# при добавлении необходимо указать параметр bulk =False
# apple.product_set.add(ipad, bulk =False)


# apple = Company.objects.get(id=1)

# print(apple.product_set.all())

# c = Company.objects.all()
# for el in c:
#     el.delete()

# создадим курс
python = Course.objects.get(id=2)

# # создадим двух студентов
tom = Student.objects.get(id=3)
sam = Student.objects.get(id=4)

# создаем поступления студентов на курс
# tom_python = Enrollment(student = tom, course= python,
#                 date=datetime.datetime.now(), mark = 5)
# sam_python = Enrollment(student = sam, course= python,
#                 date=datetime.datetime.now(), mark = 4)
# сохраняем поступления в бд
# tom_python.save()
# sam_python.save()

# получаем все курсы у Toma
tom_courses = tom.courses.all()
print(tom_courses[0].name)      # python
    
# получим всех студентов курса по python
python_students = python.students.all()
print(python_students[0].name)      # Tom
print(python_students)      # Tom

python_enrollment = python.enrollment_set.all()
print(python_enrollment)      # Tom

student_enrollment = tom.enrollment_set.all()
print(student_enrollment)      # Tom

student_enrollment = python_students[0].enrollment_set.all()
print(student_enrollment)      # Tom

# bob.courses.add(django, through_defaults={"date": date.today(), "mark": 5})
# # создаем курс для студента bob
# bob.courses.create(name="C++", through_defaults={"date": date.today(), "mark": 4})
     
# # получаем все курсы Boba
# print(bob.courses.all().values_list()) # <QuerySet [(11, 'Django'), (14, 'C++')]>
 
# # переустанавливаем курсы для студента bob
# bob.courses.set([python, java], through_defaults={"date": date.today(), "mark": 4})


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

def index_companies(request):
    products = Product.objects.all()
    return render(request, "comp.html", {"products": products})
 
# добавление данных из бд
def create_companies(request):
    # добавление начальных данных в таблицу компаний
    if Company.objects.all().count() == 0:
        Company.objects.create(name = "Apple")
        Company.objects.create(name = "Asus")
        Company.objects.create(name = "MSI")

 
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.company_id = request.POST.get("company")
        product.save()
        return HttpResponseRedirect("/comp/")
    # передаем данные в шаблон
    companies = Company.objects.all()
    return render(request, "create_comp.html", {"companies": companies})
 
# изменение данных в бд
def edit_companies(request, id):
    try:
        product = Product.objects.get(id=id)
 
        if request.method == "POST":
            product.name = request.POST.get("name")
            product.price = request.POST.get("price")
            product.company_id = request.POST.get("company")
            product.save()
            return HttpResponseRedirect("/comp/")
        else:
            companies = Company.objects.all()
            return render(request, "edit_comp.html", {"product": product, "companies": companies})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
     
# удаление данных из бд
def delete_companies(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/comp")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
 

def person(request):
    people = Person.objects.all()
    return render(request, "person.html", {"people": people})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/person/")
 
# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
 
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/person/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/person/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

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