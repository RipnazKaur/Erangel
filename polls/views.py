from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    print(request.user)
    template_name='polls/index.html'
    return render(request,template_name)

# Create your views here.
