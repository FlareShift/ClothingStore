from django.urls import path
from .views import performance_view

urlpatterns = [
    path('', performance_view, name='performance_dashboard'),
]
