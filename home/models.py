from django.db.models import CharField, ManyToManyField, Model


class Tag(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name


class Technology(Model):
    name = CharField(max_length=30)

    def __str__(self):
        return self.name


class Problem(Model):
    name = CharField(max_length=50, null=True)
    topic = CharField(max_length=50, null=True)
    description = CharField(max_length=200, null=True)
    tags = ManyToManyField(Tag)
    technologies = ManyToManyField(Technology)
    identifier = CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
