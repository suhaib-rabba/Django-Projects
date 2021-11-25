from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def trail_view(request):
    return  HttpResponse("this is the trail application view")
