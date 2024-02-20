from django import forms
from .models import Department, Person

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'parent_department']
        widgets = {
            'parent_department': forms.Select(attrs={'class': 'form-control'}),
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'department']
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
        }
