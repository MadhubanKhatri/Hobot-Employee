from django.urls import path
from .views import (
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDeleteView
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("employees/", EmployeeListCreateView.as_view(), name="employees"),
    path("employees/<int:pk>/", EmployeeRetrieveUpdateDeleteView.as_view(), name="employee-detail"),
]

urlpatterns += [
    path("token/", TokenObtainPairView.as_view()),
]