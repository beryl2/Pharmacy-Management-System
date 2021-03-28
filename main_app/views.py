from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from main_app import models

# create your views here

# from .models import *
# from .forms import OrderForm, CreateUserForm
# from .filters import OrderFilter
# from .decorators import unauthenticated_user, allowed_users, admin_only



def indexView(requests):
    medicine = models.Medicine.objects.all
    company = models.Company.objects.all
    companyAcc = models.CompanyAcconut.objects.all
    companyBank = models.CompanyBank.objects.all
    med_details = models.MedicalDetails.objects.all
    employee = models.Employee.objects.all
    employeeSalary = models.EmployeeSalary.objects.all
    employeeBank = models.EmployeeBank.objects.all
    custumer = models.Customer.objects.all
    custumerrequest = models.CustomerRequest.objects.all
    bill = models.Bill.objects.all 
    billdetails = models.BillDetails.objects.all

    context = {'medicine':medicine, 'company':company, 'companyAcc':companyAcc, 'med_details':med_details, 'employee':employee, 'employeeSalary':employeeSalary, 
    'companyBank':companyBank, 'custumer':custumer, 'employeeBank':employeeBank, 'custumerrequest':custumerrequest, 'billdetails':billdetails,'bill':bill}

    return render(requests, 'main_site/index.html', context)

def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'main_site/login.html', context)
