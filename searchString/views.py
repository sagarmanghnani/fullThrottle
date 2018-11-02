from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings 


# Create your views here.

def index(request):
    return HttpResponse("hello, world") 

def checkdata(request):
    file = open(os.path.join(settings.PROJECT_ROOT, 'word_search.tsv'))
    print(file.read())
    return HttpResponse(file.read())