import os
from django.core.exceptions import ValidationError
from django.conf import settings
from pathlib import Path

def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise ValidationError('Only CSV files are allowed.')

