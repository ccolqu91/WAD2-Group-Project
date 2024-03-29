import os
from django.core.exceptions import ValidationError
from django.conf import settings
from pathlib import Path

def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise ValidationError('Only CSV files are allowed.')

def menu_upload_to(instance, filename):
    media_path = settings.MEDIA_ROOT
    media_path= media_path.replace("\\","/")
    parent_directory_path = os.path.join(media_path, 'menus')

    if not os.path.exists(parent_directory_path):
        os.makedirs(parent_directory_path)

    directory_path = os.path.join(parent_directory_path, instance.slug)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file_path = os.path.join(directory_path, filename)
    return file_path

def logo_upload_to(instance, filename):
    media_path = settings.MEDIA_ROOT
    media_path= media_path.replace("\\","/")
    parent_directory_path = os.path.join(media_path, 'logos')

    if not os.path.exists(parent_directory_path):
        os.makedirs(parent_directory_path)

    directory_path = os.path.join(parent_directory_path, instance.slug)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file_path = os.path.join(directory_path, filename)
    return file_path