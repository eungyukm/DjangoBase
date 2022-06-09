from curses import def_prog_mode
from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def board_main(request) :
    template = loader.get_template('board_main.html')
    return HttpResponse(template.render())

# board/board_modify
def board_modify(request) :
    template = loader.get_template('board_modify.html')
    return HttpResponse(template.render())

# board/board_read
def board_read(request):
    template = loader.get_template('board_write.html')
    return HttpResponse(template.render())

# board/board_write
def board_write(request):
    template = loader.get_template('board_write.html')
    return HttpResponse(template.render())