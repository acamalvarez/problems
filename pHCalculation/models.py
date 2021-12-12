from django.db import models


class Compound(models.Model):
    name = models.CharField(max_length=20, null=True)
    formula = models.CharField(max_length=20, null=True)
    compound_type = models.CharField(max_length=20, null=True)
    k = models.FloatField(null=True)
    value = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
