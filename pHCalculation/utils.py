import numpy as np
import pandas as pd


class pH:
    def __init__(self, c0):
        self.c0 = c0

    def weak_acid(self, Ka):
        H3O = np.roots([1, Ka, -self.c0 * Ka])
        x = [i for i in H3O if i > 0]

        pH = -np.log10(x)

        return round(float(pH), 2)

    def weak_base(self, Kb):
        OH = np.roots([1, Kb, -self.c0 * Kb])
        x = [i for i in OH if i > 0]

        pOH = -np.log10(x)
        pH = 14 - pOH

        return round(float(pH), 2)

    def strong_acid(self):
        pH = -np.log10(self.c0)
        return round(float(pH), 2)

    def strong_base(self):
        pOH = -np.log10(self.c0)
        pH = 14 - pOH
        return round(float(pH), 2)


def calculate_pH(compound_value, concentration):

    data = pd.read_csv('static/pHCalculation/data.csv', index_col='id')

    compound_type = data[(data['Value'] == compound_value)]['Type'].values[0]
    k = data[(data['Value'] == compound_value)]['k'].values[0]

    if compound_type == 'weak acid':
        return pH(concentration).weak_acid(k)
    elif compound_type == 'weak base':
        return pH(concentration).weak_base(k)
    elif compound_type == 'strong acid':
        print(pH(concentration).strong_acid())
        return pH(concentration).strong_acid()
    elif compound_type == 'strong base':
        return pH(concentration).strong_base()
