from django.urls import path


from . import views


urlpatterns = [
    path('hello/', views.hello_world, name = 'hello_page'),
    path('home/', views.employeelist, name = 'homepage'),
    path('about/', views.aboutpage, name= 'aboutpage'),
    path('', views.mainpage, name = 'mainpage'),
    path('newemployee/', views.addNewEmployee, name = 'addemployee'),
    path('employeesearch/', views.employeesearch, name = 'employeesearch')
]