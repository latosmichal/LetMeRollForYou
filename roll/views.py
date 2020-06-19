from django.shortcuts import render
import random

from roll.randoms import get_roll_from_random

def roll_main(request):
    if request.method == 'GET':
        k = request.GET.get('k')
        if k:
            print(k)
            print(get_roll_from_random(k=k, n=1)[0])
            # wziąć wynik i wcisnąć w template
            return render(request, 'roll/roll_main.html', {})
        else:
            return render(request, 'roll/roll_main.html', {})

    # co jak post?
    return render(request, 'roll/roll_main.html', {})
        
        


def get_roll(request):    
    roll = random.randint(1,6)
    context = {}
    context['roll'] = roll
    return render(request, 'roll/roll_main.html', context)