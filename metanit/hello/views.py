from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

arr = [1,2,3]
 
def index(request):
    return HttpResponse("Hello " + str(datetime.datetime.now()) + " METANIT.COM " + str(arr[1]))

def i1(request):
    return HttpResponse("<h1>Hello 1 METANIT.COM</h1>")