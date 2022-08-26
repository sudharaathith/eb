
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

def index(request: HttpRequest):
  template = loader.get_template('index.html')
  context = {
    'domine' : 'hi'
  }
  return HttpResponse(template.render(context, request))
# Create your views here.
