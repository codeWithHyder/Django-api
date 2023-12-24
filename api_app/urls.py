from django.urls import path
from .views import EmployeesListCreateView

urlpatterns = [
    path('api_app/', EmployeesListCreateView.as_view(), name='api_app'),
]