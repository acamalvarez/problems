from django.shortcuts import render

from .utils import solve_problem


def home(request):

    CA0 = 1.0
    CB0 = 1.0
    k1A = 5.0
    k2A = 2.0
    k3B = 10.0
    k4C = 5.0

    CT0 = CA0 + CB0

    try:
        if (request.POST['CA0'] and
            request.POST['CB0'] and
            request.POST['k1A'] and
            request.POST['k2A'] and
            request.POST['k3B'] and
            request.POST['k4C'] and
                request.POST['CT0']):

            CA0 = float(request.POST['CA0'])
            CB0 = float(request.POST['CB0'])
            k1A = float(request.POST['k1A'])
            k2A = float(request.POST['k2A'])
            k3B = float(request.POST['k3B'])
            k4C = float(request.POST['k4C'])

            CT0 = float(request.POST['CA0']) + float(request.POST['CB0'])

    except Exception as e:
        print("ERROR", e)

    graph = solve_problem(k1A, k2A, k3B, k4C, CA0, CB0)

    context = {
        'CA0': CA0,
        'CB0': CB0,
        'k1A': k1A,
        'k2A': k2A,
        'k3B': k3B,
        'k4C': k4C,
        'CT0': CT0,
        'graph': graph,
    }

    return render(request, 'reactionsODEs/index.html', context)
