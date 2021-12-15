from django.shortcuts import render
from django.http import HttpResponse

from CandidateFinder.models import *
from django.db.models import Count

def index(request):
    workList = Job.objects.all() 
    print(workList)
    context = {"workList": workList}
    return render(request, "index.html", context)

