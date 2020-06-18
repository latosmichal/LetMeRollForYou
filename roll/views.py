from django.shortcuts import render
import random

def roll_main(request):    
    return render(request, 'roll/roll_main.html', {})


def get_roll(request):    
    roll = random.randint(1,6)
    context = {}
    context['roll'] = roll
    return render(request, 'roll/roll_main.html', context)