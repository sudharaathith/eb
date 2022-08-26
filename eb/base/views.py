
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from requests import Request, request

def index(request: Request):
  template = loader.get_template('index.html')
  context = {
    'domine' : request.headers['Host']
  }
  return HttpResponse(template.render(context, request))
# Create your views here.
