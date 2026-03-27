from django import forms 
from .models import employee
from .validate import validate_name

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['emp_id', 'fname', 'lname', 'email', 'address']



class SearchForm(forms.Form):
    FIELD_CHOICES = [
        ('fname', 'Fname'),
        ('lname', 'Lname'),
    ]


    search_field = forms.ChoiceField(
        choices=FIELD_CHOICES,
        widget= forms.RadioSelect,
        label= "Select your search Field",)
    


class EmployeeHideForm(forms.Form):
    empid = forms.IntegerField(label='Employee ID', min_value=1000)


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean(self):
        fname = self.cleaned_data['first_name']
        lname = self.cleaned_data['last_name']

        validate_name(fname)
        validate_name(lname)
        return self.cleaned_data