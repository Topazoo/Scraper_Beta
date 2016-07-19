from django.shortcuts import render
from .models import JobListing
import json
import os

def populate():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'templates', 'scrape', 'jobs2.json')
    fle = open(file_path, 'r')
    decoded = json.load(fle)

    return decoded

def jobs(request):
    
    all_jobs = populate()
    return render(request, 'scrape/job.html', {'object_list' : all_jobs})
