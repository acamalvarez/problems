from django.shortcuts import render

from .models import Compound
from .utils import calculate_pH


def home(request):
    compounds = Compound.objects.all()
    concentration = float(request.POST.get("concentration", 0.1))
    compound_value = request.POST.get("compounds_list", "Acetic_acid")

    pH = calculate_pH(compound_value, concentration)

    context = {
        "concentration": concentration,
        "compounds": compounds,
        "pH": pH,
        "compound_value": compound_value,
    }

    return render(request, "pHCalculation/index.html", context)
