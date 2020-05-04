from django.shortcuts import render
from django.http import Http404

def index(request):
    context = {'divisors': [1,2]}
    return render(request, 'index.html', context)


# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")