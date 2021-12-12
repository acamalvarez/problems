import csv

from home.models import Problem, Tag, Technology


def run():

    fhand = open('static/home/problems.csv')
    reader = csv.reader(fhand)
    next(reader)

    Problem.objects.all().delete()
    Tag.objects.all().delete()
    Technology.objects.all().delete()

    for row in reader:
        try:
            id = row[0]
            name = row[1]
            topic = row[2]
            description = row[3]
            # tags = row[4]
            # technologies = row[5]
            identifier = row[6]
        except:
            id = None
            name = None
            topic = None
            description = None
            # tags = None
            # technologies = None
            identifier = None

        tag, created = Tag.objects.get_or_create(name=row[4])
        technology, created = Technology.objects.get_or_create(name=row[5])

        problem, created = Problem.objects.get_or_create(
            id=id,
            name=name,
            topic=topic,
            description=description,
            identifier=identifier,
        )

        problem.tags.add(tag)
        problem.technologies.add(technology)

        problem.save()

# For updating the product list run the following script
# python manage.py runscript problems_load
