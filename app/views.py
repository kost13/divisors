from django.shortcuts import render

import divisors

def index(request):
    try:
        num = request.POST['number']
        divisiors_list = compute_divisiors(int(num))
    except(KeyError, ValueError):
        num = 0
        divisiors_list = []    
    context = {'divisors': divisiors_list, 'number': num}
    return render(request, 'index.html', context)

def compute_divisiors(n):
    return divisors.compute_divisors(n)
