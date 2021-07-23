from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requests):
    return HttpResponse("<center><h2><a href='/cicdpage'>Greetings, we are on a first page ""<a></h2></center>")