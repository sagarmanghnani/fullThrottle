from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings 
import csv


# Create your views here.

def index(request):
    return HttpResponse("hello, world") 

def checkdata(request):
    superfile = open(os.path.join(settings.PROJECT_ROOT, 'word_search.tsv'))
    s = superfile.readline()
    p = s.split(' ')
    print(p)
    return HttpResponse("check")