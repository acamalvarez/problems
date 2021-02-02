from django.contrib import admin

from .models import Problem, Tag, Technology

admin.site.register(Problem)
admin.site.register(Tag)
admin.site.register(Technology)
