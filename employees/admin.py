from xml.sax import default_parser_list

from django.contrib import admin
from .models import Department, Position, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'department', 'created_at')
    list_filter = ('level', 'department')
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'departament', 'position', 'is_active', 'hire_date')
    list_filter = ('is_active', 'departament', 'position')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name')






