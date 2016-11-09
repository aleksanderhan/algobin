from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def create_paste(request):
    template = loader.get_template('algobin/create_paste.html')
    return HttpResponse(template.render(request))


def detail(request, algorithm_id):
    response = "You're looking at algorithm " + algorithm_id
    return HttpResponse(response)