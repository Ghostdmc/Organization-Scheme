from django.contrib import admin
from .models import Department, Person

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_department')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

