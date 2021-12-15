from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse

from .models import *

def find_candidate(request, job_title):
    """Find the best candidate for a job"""
    matching_title_candidates = Candidate.objects.filter(title=job_title)
    job_skills = Job.object.get(title = job_title).skills.all()
    print(job_skills)
    matching_candidates = matching_title_candidates.filter(skills__in=job_skills)
    print(matching_candidates)
    sorted_matching_candidates = matching_candidates.annotate(count = Count('name')).order_by('-count')
    print(sorted_matching_candidates)

    return HttpResponse(f'List of skills = {queryset_to_str(job_skills)}')

def queryset_to_str(queryset):
    arr = []
    for query in queryset:
        arr.append(str(query))
    return arr
