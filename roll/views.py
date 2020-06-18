from django.shortcuts import render

def roll_main(request):
    return render(request, 'roll/roll_main.html', {})
