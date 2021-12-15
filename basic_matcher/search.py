from CandidateFinder.models import *
from django.db.models import Count
skills_of_job0 = Job.objects.all()[0].skills.all()
print(skills_of_job0)
list_of_matching_candidates = Candidate.objects.filter(skills__in=skills_of_job0)
print(list_of_matching_candidates)
sorted_list = list_of_matching_candidates.annotate(count = Count('name')).order_by('-count')
print(sorted_list)
print('With count:')
for candidate in sorted_list:
    print(candidate,candidate.count)

#exec(open('search.py').read())