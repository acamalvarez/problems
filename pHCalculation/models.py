from django.db.models import CharField, FloatField, Model


class Compound(Model):
    name = CharField(max_length=20, null=True)
    formula = CharField(max_length=20, null=True)
    compound_type = CharField(max_length=20, null=True)
    k = FloatField(null=True)
    value = CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
