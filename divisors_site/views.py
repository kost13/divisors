# project: Divisors
# author: Lukasz Kostrzewa

"""divisors_site view configuration
"""
from django.shortcuts import render
import divisors

def index(request):
    """
    Generates the main page. If the request contains a number,
    its dividors are computed and displayed. Otherwise only a 
    form to enter the number is displayed.
    """
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
