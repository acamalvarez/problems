import csv

from pHCalculation.models import Compound

def run():

    fhand = open('static/pHCalculation/data.csv')
    reader = csv.reader(fhand)
    next(reader)

    Compound.objects.all().delete()

    for row in reader:
        try:
            id = row[0]
            name = row[1]
            formula = row[2]
            compound_type = row[3]
            k = float(row[4])
            value = row[5]
        except:
            id = None
            name = None
            formula = None
            compound_type = None
            k = None
            value = None

        compound, created = Compound.objects.get_or_create(
            id=id, 
            name=name, 
            formula=formula,
            compound_type=compound_type,
            k = k,
            value=value,)

        compound.save()

# For updating the product list run the following script
# python manage.py runscript compound_load