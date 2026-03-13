from django import forms 
from .models import employee


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