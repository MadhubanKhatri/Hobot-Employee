# HabotConnect API

Employee management API built with Django REST Framework.

## Project Overview

This is a RESTful API for managing employee records with features including:
- List, create, retrieve, update, and delete employees
- Pagination support
- Filter by department and role
- Email uniqueness validation
- Input validation (non-empty names)

## Project Structure

```
├── api/                 # API app
│   ├── models.py        # Employee model
│   ├── serializers.py   # DRF serializers
│   ├── views.py         # API viewsets
│   ├── urls.py          # URL routing
│   └── tests.py         # Test cases
├── settings.py          # Django settings
├── urls.py              # Main URL config
└── manage.py            # Django CLI
└── README.md
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   cd e:\HabotConnect\ Assessment\habotconnect_api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Employees
- `GET /api/employees/` - List all employees (paginated, 4 per page)
- `POST /api/employees/` - Create new employee
- `GET /api/employees/{id}/` - Retrieve specific employee
- `PATCH /api/employees/{id}/` - Update employee
- `DELETE /api/employees/{id}/` - Delete employee

### Query Parameters
- `?department=IT` - Filter by department
- `?role=Developer` - Filter by role

## Running Tests

Execute the test suite:

```bash
python manage.py test api.tests
```

### Test Coverage

- **EmployeeListTests**: Pagination, creation, filtering, validation
- **EmployeeDetailTests**: Retrieval, update, deletion

## Request/Response Examples

### Create Employee
```bash
POST /api/employees/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@test.com",
  "department": "HR",
  "role": "Manager"
}
```

### Filter Employees
```bash
GET /api/employees/?department=IT&role=Developer
```

## Validation Rules

- **Email**: Must be unique
- **Name**: Cannot be empty or whitespace only
- **All fields**: Required
