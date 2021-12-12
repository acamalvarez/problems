from django.shortcuts import render

from .models import Compound
from .utils import calculate_pH


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

    pH = calculate_pH(compound_value, concentration)

    context = {
        'concentration': concentration,
        'compounds': compounds,
        'pH': pH,
        'compound_value': compound_value,
    }

    return render(request, 'pHCalculation/index.html', context)
