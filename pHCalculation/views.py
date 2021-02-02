from django.shortcuts import render
from django.http import HttpResponse

from .utils import calculatepH

from .models import Compound

def home(request):

    compounds = Compound.objects.all()

    try:
        if request.method == 'POST':
            concentration = float(request.POST.get('concentration'))
            compound_value = request.POST.get('compounds_list')
        else:
            concentration = 0.1
            compound_value = 'Acetic_acid'
    
    except Exception as e:
        print('ERROR', e)

    pH = calculatepH(compound_value, concentration)

    context = {
        'concentration':concentration,
        'compounds': compounds,
        'pH': pH,
        'compound_value': compound_value,
    }

    return render(request, 'pHCalculation/index.html', context)
