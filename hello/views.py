from django.shortcuts import render
from django.http import HttpResponse

import requests

from .models import Greeting

# Create your views here.
def index(request):
    # r = requests.get('http://httpbin.org/status/418')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')
    return render(request, 'chart1.html')

def chart2(request):
    return render(request,'chart2.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

