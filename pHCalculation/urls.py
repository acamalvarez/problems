from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='pHCalculation'),
    # path('result/', views.pH, name="pHResult"),
]