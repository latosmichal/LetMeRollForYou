from django.shortcuts import render
from django.http import HttpResponseNotAllowed
import random

from roll.randoms import get_roll_from_random

def roll_main(request):
    if request.method == 'GET':
        k = request.GET.get('k')    
        print(k)    
        if k:
            roll=get_roll_from_random(k=k, n=1)[0]
            return render(request, 'roll/roll_main.html', {'roll':roll})
        else:
            return render(request, 'roll/roll_main.html', {})

    # co jak post?    
    return HttpResponseNotAllowed('GET')