from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Person
from .forms import DepartmentForm, PersonForm
from django.views import View
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic.edit import DeleteView

class DepartmentListView(View):
    def get(self, request):
        departments = Department.objects.all()
        return render(request, 'organization_scheme/department_list.html', {'departments': departments})

class DepartmentCreateView(View):
    def get(self, request):
        form = DepartmentForm()
        return render(request, 'organization_scheme/department_form.html', {'form': form})

    def post(self, request):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department-list')
        return render(request, 'organization_scheme/department_form.html', {'form': form})

class DepartmentUpdateView(View):
    def get(self, request, pk):
        department = get_object_or_404(Department, id=pk)
        form = DepartmentForm(instance=department)
        return render(request, 'organization_scheme/department_form.html', {'form': form})

    def post(self, request, pk):
        department = get_object_or_404(Department, id=pk)
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department-list')
        return render(request, 'organization_scheme/department_form.html', {'form': form})

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'organization_scheme/department_confirm_delete.html'
    success_url = reverse_lazy('department-list')

class PersonListView(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(request, 'organization_scheme/person_list.html', {'persons': persons})

class PersonCreateView(View):
    def get(self, request):
        form = PersonForm()
        return render(request, 'organization_scheme/person_form.html', {'form': form})

    def post(self, request):
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('person-list')
        return render(request, 'organization_scheme/person_form.html', {'form': form})

class PersonUpdateView(View):
    def get(self, request, pk):
        person = get_object_or_404(Person, id=pk)
        form = PersonForm(instance=person)
        return render(request, 'organization_scheme/person_form.html', {'form': form})

    def post(self, request, pk):
        person = get_object_or_404(Person, id=pk)
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person-list')
        return render(request, 'organization_scheme/person_form.html', {'form': form})

class PersonDeleteView(DeleteView):
    model = Department
    template_name = 'organization_scheme/person_confirm_delete.html'
    success_url = reverse_lazy('person-list')
    

class OrganizationStructureView(View):
    def get(self, request):
        departments = Department.objects.all()
        persons = Person.objects.all()

        context = {
            'departments': departments,
            'persons': persons,
        }

        return render(request, 'organization_scheme/organization_structure.html', context)