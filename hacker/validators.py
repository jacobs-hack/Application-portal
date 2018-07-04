def validate_extension(valid_extensions):
    def validate_file_extension(value):
        import os
        from django.core.exceptions import ValidationError
        ext = os.path.splitext(value.name)[1]
        if not ext.lower() in valid_extensions:
            raise ValidationError(u'File Extension not allowed: Must be one of {}.'.format(','.join(map(repr, valid_extensions))))
    return validate_file_extension