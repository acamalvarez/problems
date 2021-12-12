from django.shortcuts import render

from .utils import solve_problem


def home(request):
    CA0 = float(request.POST.get('CA0', 1))
    CB0 = float(request.POST.get('CB0', 1))
    k1A = float(request.POST.get('k1A', 5))
    k2A = float(request.POST.get('k2A', 2))
    k3B = float(request.POST.get('k3B', 10))
    k4C = float(request.POST.get('k4C', 5))

    CT0 = CA0 + CB0

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
