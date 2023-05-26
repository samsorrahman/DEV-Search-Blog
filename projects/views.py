from django.shortcuts import render
from django.http import HttpResponse
from . models import Project
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    context = {
        'projectobj': projectobj,

    }
    return render(request, 'projects/single-project.html', context)
