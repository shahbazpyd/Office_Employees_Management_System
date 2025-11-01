"""
URL configuration for office_emp_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_emp', views.all_emp, name='all_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
    # path('remove_emp/', views.remove_emp, name='remove_emp_list'),
    # path('remove_emp/<int:emp_id>/', views.remove_emp, name='remove_emp_confirm'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('create_department/', views.create_department, name='create_department'),
    path('create_role/', views.create_role, name='create_role'),
]
