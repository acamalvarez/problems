from django.shortcuts import render

from .utils import solve_lin_prog


def home(request):

    costPaintA = float(request.POST.get('costPaintA', 1120))
    costPaintB = float(request.POST.get('costPaintB', 1596))
    costPaintC = float(request.POST.get('costPaintC', 1764))

    pigmentA = float(request.POST.get('pigmentA', 72))
    pigmentB = float(request.POST.get('pigmentB', 28))
    pigmentC = float(request.POST.get('pigmentC', 25))
    pigmentConstraint = float(request.POST.get('pigmentConstraint', 1700))

    binderA = float(request.POST.get('binderA', 5))
    binderB = float(request.POST.get('binderB', 35))
    binderC = float(request.POST.get('binderC', 45))
    binderConstraint = float(request.POST.get('binderConstraint', 1500))

    solventA = float(request.POST.get('solventA', 50))
    solventB = float(request.POST.get('solventB', 30))
    solventC = float(request.POST.get('solventC', 35))
    solventConstraint = float(request.POST.get('solventConstraint', 1100))

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
