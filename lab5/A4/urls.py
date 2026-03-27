from django.urls import path


from . import views


urlpatterns = [
    path('hello/', views.hello_world, name = 'hello_page'),
    path('home/', views.employeelist, name = 'homepage'),
    path('about/', views.aboutpage, name= 'aboutpage'),
    path('', views.mainpage, name = 'mainpage'),
    path('newemployee/', views.addNewEmployee, name = 'addemployee'),
    path('employeesearch/', views.employeesearch, name = 'employeesearch'),
    path('hide/', views.employeehide, name = 'employeehide'),
    path('registration/', views.registration_page, name ='registration'),
    path('login/', views.login_page, name = 'login'),
    path('logout/', views.logout_user, name = 'logout')
]