from django.shortcuts import render

from django.http import HttpResponse


def paste_algo(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, algorithm_id):
	response = "You're looking at algorithm " + algorithm_id
	return HttpResponse(response)