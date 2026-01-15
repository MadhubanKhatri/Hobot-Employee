from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeePagination(PageNumberPagination):
    page_size = 4


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by("id")
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = EmployeePagination

    def get_queryset(self):
        queryset = super().get_queryset()
        department = self.request.query_params.get("department")
        role = self.request.query_params.get("role")

        # Department filter
        if department:
            queryset = queryset.filter(department__iexact=department)

        # Role filter
        if role:
            queryset = queryset.filter(role__iexact=role)

        return queryset


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
