from django.urls import path, include

from . import views

from home.views import ProblemsListView

app_name='home'
urlpatterns = [
    path('', ProblemsListView.as_view(), name='index')
]
