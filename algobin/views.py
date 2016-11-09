from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import AlgorithmForm


def submit_algorithm(request):
    '''
    template = loader.get_template('algobin/create_paste.html')
    return HttpResponse(template.render(request))
    '''
    if request.method =='POST':
        form = AlgorithmForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('.')

    else:
        form = AlgorithmForm()

    return render(request, 'algobin/submit_algorithm.html', {'form' : form})


def detail(request, algorithm_id):
    response = "You're looking at algorithm " + algorithm_id
    return HttpResponse(response)