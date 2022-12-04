from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import  RegexValidator

def number_only(value):
    RegexValidator(r'^[0-9]*$', 'Somente números.').__call__(value)

