from django.shortcuts import render
from django.http import Http404

def index(request):
    try:
        num = request.POST['number']
        divisiors = compute_divisiors(int(num))
    except(KeyError, ValueError):
        divisiors = []    
    context = {'divisors': divisiors}
    return render(request, 'index.html', context)

def compute_divisiors(num):
    nums = []
    for i in range(num):
        nums.append(i)
    return nums
