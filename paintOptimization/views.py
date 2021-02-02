from django.shortcuts import render

from .utils import solve_lin_prog

def home(request):

    costPaintA = 1120.0
    costPaintB = 1596.0
    costPaintC = 1764.0

    pigmentA = 72.0
    pigmentB = 28.0
    pigmentC = 25.0
    pigmentConstraint = 1700.0

    binderA = 5.0
    binderB = 35.0
    binderC = 45.0
    binderConstraint = 1500.0

    solventA = 50.0
    solventB = 30.0
    solventC = 35.0
    solventConstraint = 1100.0

    try:
        if (request.POST['costPaintA'] and
            request.POST['costPaintB'] and
            request.POST['costPaintC'] and
            request.POST['pigmentA'] and
            request.POST['pigmentB'] and
            request.POST['pigmentC'] and
            request.POST['pigmentConstraint'] and
            request.POST['binderA'] and
            request.POST['binderB'] and
            request.POST['binderC'] and
            request.POST['binderConstraint'] and
            request.POST['solventA'] and
            request.POST['solventB'] and
            request.POST['solventC'] and
            request.POST['solventConstraint']):

            costPaintA = float(request.POST['costPaintA'])
            costPaintB = float(request.POST['costPaintB'])
            costPaintC = float(request.POST['costPaintC'])

            pigmentA = float(request.POST.get('pigmentA'))
            pigmentB = float(request.POST.get('pigmentB'))
            pigmentC = float(request.POST.get('pigmentC'))
            pigmentConstraint = float(request.POST.get('pigmentConstraint'))

            binderA = float(request.POST.get('binderA'))
            binderB = float(request.POST.get('binderB'))
            binderC = float(request.POST.get('binderC'))
            binderConstraint = float(request.POST.get('binderConstraint'))

            solventA = float(request.POST.get('solventA'))
            solventB = float(request.POST.get('solventB'))
            solventC = float(request.POST.get('solventC'))
            solventConstraint = float(request.POST.get('solventConstraint'))

    except Exception as e:
        print('ERROR', e)

    solution = solve_lin_prog([costPaintA, costPaintB, costPaintC],
        [[-pigmentA, -pigmentB, -pigmentC], 
        [-binderA, -binderB, -binderC], 
        [-solventA, -solventB, -solventC]],
        [-pigmentConstraint, -binderConstraint, -solventConstraint]).x

    paintA = round(solution[0], 1)
    paintB = round(solution[1], 1)
    paintC = round(solution[2], 1)

    context = {
        'costPaintA': costPaintA,
        'costPaintB': costPaintB,
        'costPaintC': costPaintC,
        'pigmentA': pigmentA,
        'pigmentB': pigmentB,
        'pigmentC': pigmentC,
        'pigmentConstraint': pigmentConstraint,
        'binderA': binderA,
        'binderB': binderB,
        'binderC': binderC,
        'binderConstraint': binderConstraint,
        'solventA': solventA,
        'solventB': solventB,
        'solventC': solventC,
        'solventConstraint': solventConstraint,
        'paintA': paintA,
        'paintB': paintB,
        'paintC': paintC,
    }

    return render(request, 'paintOptimization/index.html', context)
