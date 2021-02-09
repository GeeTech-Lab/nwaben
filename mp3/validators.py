import os


def validate_file_extension(value):
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.midi', 'wma']
    if ext.lower() not in valid_extensions:
        raise ValidationError('This is not a music file format.')
