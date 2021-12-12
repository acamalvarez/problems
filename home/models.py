from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.CharField(max_length=50, null=True)
    topic = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag)
    technologies = models.ManyToManyField(Technology)
    identifier = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
