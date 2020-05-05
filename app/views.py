from django.shortcuts import render
from django.http import Http404

def index(request):
    try:
        num = request.POST['number']
        divisiors = compute_divisiors(int(num))
    except(KeyError, ValueError):
        num = 0
        divisiors = []    
    context = {'divisors': divisiors, 'number': num}
    return render(request, 'index.html', context)

import math
def compute_divisiors(n):
    nums = []

    i = int(math.sqrt(n))
    while i > 0: 
          
        if (n % i == 0) : 
              
            # If divisors are equal, print only one 
            if (n / i == i) : 
                nums.append(i), 
            else : 
                # Otherwise print both 
                nums.append(i)
                nums.append(int(n/i)), 
        i = i - 1
    return nums