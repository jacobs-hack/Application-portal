# https://code.djangoproject.com/ticket/22999
### This file is broken, but still needed by some of the old migrations

from django.utils.deconstruct import deconstructible
import os
from django.core.exceptions import ValidationError

@deconstructible
class FileExtensionValidator(object):
    def __init__(self, valid_ext):
        self.valid_ext = valid_ext
    def __call__(self, instance, filename):
        ext = os.path.splitext(filename.name)[1]
        if not ext.lower() in self.valid_ext:
            raise ValidationError(
                u'File Extension not allowed: Must be one of {}.'.format(','.join(map(repr, self.valid_ext))))


validate_extension = FileExtensionValidator([".pdf"])
