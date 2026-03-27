from django.db import models
from .validate import validate_name, validate_email
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class employee(models.Model):
    emp_id = models.IntegerField(primary_key=True, null=False, blank=False, validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    fname = models.CharField(max_length=50, null=False, blank=False, validators=[validate_name])
    lname = models.CharField(max_length=50, null=False, blank=False, validators=[validate_name])
    email = models.CharField(max_length=50, null=False, blank=False, validators=[validate_email])
    address = models.CharField(max_length=100, null=False, blank=False)
    visible = models.BooleanField(null=False, blank=False, default=True)


    def __str__(self):
        return str(self.emp_id) + ":" +str(self.fname) + ":" +str(self.lname) + ":" +str(self.email) + ":" +str(self.address) 