from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='addressbook-home'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('edit_contact/<id>/', views.edit_contact, name='edit_contact'),
    path('update_contact/<id>/', views.update_contact, name='update_contact'),
    path('delete_contact/<id>/', views.delete_contact, name='delete_contact'),
    path('upload-csv/', views.contact_upload, name='contact_upload'),
]
