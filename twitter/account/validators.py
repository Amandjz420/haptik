import re

from django.core.exceptions import ValidationError


def phone_regex(value):
    reg = re.compile('^\+?\d{10,12}$')
    if not reg.match(value):
        raise ValidationError(
            "Phone number must be entered in the format: '+919999999999'. enter 10 digits with internaltional code allowed."
        )