from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Employee


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def all_emp(request):
    emp_list = Employee.objects.all()
    paginator = Paginator(emp_list, 5)  # Show 5 employees per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'emps': page_obj
    }
    print(context)
    return render(request, 'view_all_emp.html', context)

@login_required
def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone,
                           dept_id=dept, role_id=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully!")
    elif request.method == "GET":
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("Something Went Wrong!")

@login_required
def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully!")
        except:
            return HttpResponse("Something Went Wrong!")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'remove_emp.html', context)

@login_required
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        print(context)
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("Something Went Wrong!")




from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # Redirect to login page after successful signup
    template_name = 'registration/signup.html'

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')