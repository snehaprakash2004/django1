from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('add_department/', views.add_department, name='add_department'),
    path('view_employees/', views.view_employees, name='view_employees'),
    path('view_departments/', views.view_departments, name='view_departments'),
    path('edit_employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('edit_department/<int:department_id>/', views.edit_department, name='edit_department'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('delete_department/<int:department_id>/', views.delete_department, name='delete_department'),
]
