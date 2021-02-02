from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.db.models import Q

from home.models import Problem

class ProblemsListView(ListView):
    model = Problem
    template_name = 'home/problem_list.html'

    def get(self, request):
        strval = request.GET.get('search', False)
        if strval:
            
            # query = Q(name__contains=strval)
            # query.add(Q(description__contains=strval), Q.OR)
            # query.add(Q(technologies__name__contains=strval), Q.OR)
            # objects = Problem.objects.filter(query).select_related()

            objects = Problem.objects.filter(
                Q(name__contains=strval)
                | Q(description__contains=strval)
                | Q(technologies__name__contains=strval)
                ).distinct()
        else:
            objects = Problem.objects.all()

        ctx = {'problem_list': objects, 'search': strval}

        return render(request, self.template_name, ctx)




# class HomeView(TemplateView):
#     template_name = "home/index.html"
