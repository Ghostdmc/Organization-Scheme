from django.urls import path
from .views import (
    DepartmentListView,
    DepartmentCreateView,
    DepartmentUpdateView,
    DepartmentDeleteView,
    PersonListView,
    PersonCreateView,
    PersonUpdateView,
    PersonDeleteView,
    OrganizationStructureView,
)

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department-create'),
    path('departments/update/<int:pk>/', DepartmentUpdateView.as_view(), name='department-update'),
    path('departments/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department-delete'),

    path('persons/', PersonListView.as_view(), name='person-list'),
    path('persons/create/', PersonCreateView.as_view(), name='person-create'),
    path('persons/update/<int:pk>/', PersonUpdateView.as_view(), name='person-update'),
    path('persons/delete/<int:pk>/', PersonDeleteView.as_view(), name='person-delete'),

    path('organization_structure/', OrganizationStructureView.as_view(), name='organization-structure'),
]
