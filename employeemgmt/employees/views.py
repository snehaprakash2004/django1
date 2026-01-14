from django.shortcuts import render
from .models import Employee, Department

# Dashboard view
def dashboard(request):
    employees_count = Employee.objects.count()
    departments_count = Department.objects.count()
    return render(request, 'dashboard.html', {
        'employees_count': employees_count,
        'departments_count': departments_count
    })


# Add employee
def add_employee(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        department = request.POST.get('department')
        Employee.objects.create(
            full_name=full_name,
            email=email,
            age=age,
            department_id=department
        )
        return render(request, 'add_employee.html', {
            'message': 'Employee added successfully!',
            'departments': Department.objects.all()
        })
    return render(request, 'add_employee.html', {'departments': Department.objects.all()})


# Add department
def add_department(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Department.objects.create(name=name)
            return render(request, 'add_department.html', {
                'message': 'Department added successfully!'
            })
    return render(request, 'add_department.html', {})


# View employees
def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'view_employees.html', {'employees': employees})


# View departments
def view_departments(request):
    departments = Department.objects.all()
    return render(request, 'view_departments.html', {'departments': departments})


# Edit employee
def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    departments = Department.objects.all()
    if request.method == 'POST':
        employee.full_name = request.POST.get('full_name')
        employee.email = request.POST.get('email')
        employee.age = request.POST.get('age')
        employee.department_id = request.POST.get('department')
        employee.save()
        return render(request, 'edit_employee.html', {
            'employee': employee,
            'departments': departments,
            'message': 'Employee updated successfully!'
        })
    return render(request, 'edit_employee.html', {
        'employee': employee,
        'departments': departments
    })


# Edit department
def edit_department(request, department_id):
    department = Department.objects.get(id=department_id)
    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.save()
        return render(request, 'edit_department.html', {
            'department': department,
            'message': 'Department updated successfully!'
        })
    return render(request, 'edit_department.html', {'department': department})


# Delete employee
def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    employees = Employee.objects.all()
    return render(request, 'view_employees.html', {
        'employees': employees,
        'message': 'Employee deleted successfully!'
    })


# Delete department
def delete_department(request, department_id):
    department = Department.objects.get(id=department_id)
    department.delete()
    departments = Department.objects.all()
    return render(request, 'view_departments.html', {
        'departments': departments,
        'message': 'Department deleted successfully!'
    })