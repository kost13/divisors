# project: Divisors
# author: Lukasz Kostrzewa

"""divisors_site URL Configuration
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]