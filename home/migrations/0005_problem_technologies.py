# Generated by Django 3.1.5 on 2021-01-28 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='technologies',
            field=models.ManyToManyField(to='home.Technology'),
        ),
    ]
