from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

# user/join
def join(request) :
    template = loader.get_template('join.html')
    return HttpResponse(template.render())

# user/login
def login(request) :
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

# user/modify_user
def modify_user(request) :
    template = loader.get_template('modify_user.html')
    return HttpResponse(template.render())