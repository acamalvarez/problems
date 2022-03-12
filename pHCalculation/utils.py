import numpy as np
import pandas as pd

COMPOUNDS_DATA = pd.read_csv("static/pHCalculation/data.csv", index_col="id")


class pH:
    def __init__(self, c0):
        self.c0 = c0

    def weak_acid(self, Ka):
        H3O = max(np.roots([1, Ka, -self.c0 * Ka]))
        pH = -np.log10(H3O)
        return round(pH, 2)

    def weak_base(self, Kb):
        OH = max(np.roots([1, Kb, -self.c0 * Kb]))
        pH = 14 + np.log10(OH)
        return round(pH, 2)

    def strong_acid(self):
        pH = -np.log10(self.c0)
        return round(pH, 2)

    def strong_base(self):
        pH = 14 + np.log10(self.c0)
        return round(pH, 2)


def calculate_pH(compound_value, concentration):
    compound_type = COMPOUNDS_DATA[(COMPOUNDS_DATA["Value"] == compound_value)][
        "Type"
    ].values[0]
    k = COMPOUNDS_DATA[(COMPOUNDS_DATA["Value"] == compound_value)]["k"].values[0]

    if compound_type == "weak acid":
        return pH(concentration).weak_acid(k)
    elif compound_type == "weak base":
        return pH(concentration).weak_base(k)
    elif compound_type == "strong acid":
        return pH(concentration).strong_acid()
    elif compound_type == "strong base":
        return pH(concentration).strong_base()
