from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse

from .models import *

def index(request):
    return HttpResponse('hi welcome to my  ')

def find_candidate(request, job_title):
    """Find the best candidate for a job"""
    print(job_title)
    matching_title_candidates = Candidate.objects.filter(title__name=job_title)
    job_skills = Job.objects.get(title__name=job_title).skills.all()
    print(job_skills)
    matching_candidates = matching_title_candidates.filter(skills__in=job_skills)
    print(matching_candidates)
    sorted_matching_candidates = matching_candidates.annotate(count = Count('name')).order_by('-count')
    print(sorted_matching_candidates)
    
    return HttpResponse(f'The best Candidate for the job = {queryset_to_str(sorted_matching_candidates)[0]} <br> sorted list = {str(queryset_to_str(sorted_matching_candidates)).strip("[|]")}')

def queryset_to_str(queryset):
    arr = []
    for query in queryset:
        arr.append(str(query))
    return arr
