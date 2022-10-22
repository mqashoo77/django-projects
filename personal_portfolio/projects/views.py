from django.shortcuts import render
from projects.models import Project

# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {'projects': projects} # data structue // as dictionary 
    return render(request, 'project_index.html', context)
