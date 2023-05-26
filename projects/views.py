from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def projects(request):
    return HttpResponse('here are the products')


def project(request, pk):
    return HttpResponse('single project' + ' ' + str(pk))
