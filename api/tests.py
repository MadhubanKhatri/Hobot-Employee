from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Employee


class EmployeeListTests(APITestCase):

    def setUp(self):
        for i in range(6):
            Employee.objects.create(
                name=f"Employee {i}",
                email=f"user{i}@test.com",
                department="IT",
                role="Developer"
            )

    def test_employee_list_paginated(self):
        url = reverse("employees")
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 4   # page_size = 4


    def test_create_employee(self):
        url = reverse("employees")
        payload = {
            "name": "John Doe",
            "email": "john@test.com",
            "department": "HR",
            "role": "Manager"
        }

        response = self.client.post(url, payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert Employee.objects.count() == 7



    def test_duplicate_email_not_allowed(self):
        url = reverse("employees")
        payload = {
            "name": "Another User",
            "email": "user0@test.com",  # already exists
            "department": "IT",
            "role": "Tester"
        }

        response = self.client.post(url, payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "email" in response.data


    def test_filter_by_department(self):
        url = reverse("employees") + "?department=IT"
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        for emp in response.data["results"]:
            assert emp["department"].lower() == "it"


    def test_filter_by_role(self):
        url = reverse("employees") + "?role=Developer"
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        for emp in response.data["results"]:
            assert emp["role"].lower() == "developer"


class EmployeeDetailTests(APITestCase):

    def setUp(self):
        self.employee = Employee.objects.create(
            name="Alice",
            email="alice@test.com",
            department="Finance",
            role="Analyst"
        )

    def test_retrieve_employee(self):
        url = reverse("employee-detail", args=[self.employee.id])
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == "alice@test.com"


    def test_update_employee(self):
        url = reverse("employee-detail", args=[self.employee.id])
        payload = {"name": "Alice Updated"}

        response = self.client.patch(url, payload)

        assert response.status_code == status.HTTP_200_OK
        self.employee.refresh_from_db()
        assert self.employee.name == "Alice Updated"


    def test_delete_employee(self):
        url = reverse("employee-detail", args=[self.employee.id])
        response = self.client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Employee.objects.count() == 0


    def test_empty_name_not_allowed(self):
        url = reverse("employees")
        payload = {
            "name": "   ",
            "email": "empty@test.com",
            "department": "IT",
            "role": "Dev"
        }

        response = self.client.post(url, payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "name" in response.data
