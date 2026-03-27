from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user

# Create your views here.

def hello_world(response):
    return HttpResponse('<h3>Hello World!</h3>')


def mainpage(request):
    return render(request, 'main.html')

def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')



from .forms import EmployeeModelForm
from django.contrib import messages

@login_required(login_url='login')
@allowed_user(allowed_groups=['Mngrs'])
def addNewEmployee(request):
    if request.method == "POST":
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'A new employee has been added')
            elist = employee.objects.all()
            return render(request, 'home.html', {'elist': elist})
        else:
            messages.error(request, ('Incorrect Info.'))
            return render(request, 'employeeentryform.html', {'form': form})
    form = EmployeeModelForm()
    return render(request, 'employeeentryform.html', {'form': form})


from .models import employee
@login_required(login_url='login')
@allowed_user(allowed_groups=['Mngrs', 'Emps'])
def employeelist(request):
    employees = employee.objects.filter(visible=True)
    return render(request, 'home.html', {'elist': employees})


from .forms import SearchForm
@login_required(login_url='login')
@allowed_user(allowed_groups=['Mngrs', 'Emps'])
def employeesearch(request):
    if request.method =='POST':
        form = SearchForm(request.POST)
        selected = request.POST.get('search_field')
        if selected == 'fname':
            sterm = request.POST['stext']
            elist = employee.objects.filter(fname__startswith=sterm, visible=True)
            return render(request, 'home.html', {'elist': elist})
        elif selected == 'lname':
            sterm = request.POST['stext']
            elist = employee.objects.filter(lname__startswith=sterm, visible=True)
            return render(request, 'home.html', {'elist': elist})


    form = SearchForm()    
    return render(request, 'employeesearch.html', {'form':form})


from .forms import EmployeeHideForm
@login_required(login_url='login')
@allowed_user(allowed_groups=['Mngrs'])
def employeehide(request):
    if request.method == 'POST':
        form = EmployeeHideForm(request.POST)
        if form.is_valid():
            sterm = form.cleaned_data['empid']
            if employee.objects.filter(emp_id=sterm, visible=True).exists(): 
                employee.objects.filter(emp_id=sterm).update(visible=False)  
                messages.success(request, f"Employee {sterm} has been hidden.") 
                elist = employee.objects.filter(visible=True)     
                return render(request, 'home.html', {'elist':elist})
            else:
                messages.error(request, f'No visible employee with ID {sterm}')
        return render(request,'employeehide.html', {'form':form})
    form = EmployeeHideForm()
    return render(request, 'employeehide.html', {'form':form})



from .forms import CreateUserForm
from django.contrib.auth.models import Group
@allowed_user(allowed_groups=['Mngrs'])
def registration_page(request):
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            user = form.cleaned_data.get('username')
            group = Group.objects.get(name='Emps')
            newuser.groups.add(group)
            messages.success(request, {f'The User {user} has been successfully added.'})
            return redirect('login')
        else:
            messages.error(request, ('Error'))
            return render(request, 'registration.html', {'form': form})
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'registration.html', context)


from django.contrib.auth import login, logout, authenticate
def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successful Login')
                return redirect('homepage')
            else:
                messages.info(request, 'Incorrect Login Info')
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')