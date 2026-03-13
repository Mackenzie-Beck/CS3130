from django.shortcuts import render
from django.http import HttpResponse

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
def employeelist(request):
    employees = employee.objects.all()
    return render(request, 'home.html', {'elist': employees})


from .forms import SearchForm
def employeesearch(request):
    if request.method =='POST':
        form = SearchForm(request.POST)
        selected = request.POST.get('search_field')
        if selected == 'fname':
            sterm = request.POST['stext']
            elist = employee.objects.filter(fname__startswith=sterm)
            return render(request, 'home.html', {'elist': elist})
        elif selected == 'lname':
            sterm = request.POST['stext']
            elist = employee.objects.filter(lname__startswith=sterm)
            return render(request, 'home.html', {'elist': elist})


    form = SearchForm()    
    return render(request, 'employeesearch.html', {'form':form})