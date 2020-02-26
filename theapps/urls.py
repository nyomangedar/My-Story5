from django.urls import path
from theapps import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('forms/', views.forms, name='forms'),
    path('data/',views.thedata, name='data'),
]