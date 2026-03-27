from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_name(value):
    if not value.isalpha():
        raise ValidationError(
            _("%(value)s is not a valid name"),
            params={'value': value},
        )
    

EMAIL_REGEX = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

def validate_email(value):
    value = (value or '').strip()
    if not EMAIL_REGEX.fullmatch(value):
        raise ValidationError(
            _("%(value)s is not a valid email address"),
            params={'value':value},
        )
    

