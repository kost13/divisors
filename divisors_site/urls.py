"""divisors_site URL Configuration
"""

from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
]