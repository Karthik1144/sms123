from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_contact, name='add_contact'),
    path('view/', views.view_contacts, name='view_contacts'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]
