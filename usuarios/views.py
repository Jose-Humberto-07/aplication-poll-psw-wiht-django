from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cadastro(request):
    #return HttpResponse('Olá Mundo, testando mais uma aplicação django')
    return render(request, 'cadastro.html')

