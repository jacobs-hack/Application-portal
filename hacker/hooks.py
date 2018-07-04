import os.path

from django.db import models
from django.dispatch import receiver

from hacker.models import CV

# These two auto-delete files from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=CV)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.cv:
        if os.path.isfile(instance.cv.path):
            os.remove(instance.cv.path)

@receiver(models.signals.pre_save, sender=CV)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
    if not instance.pk:
        return False

    try:
        old_file = CV.objects.get(pk=instance.pk).cv
    except CV.DoesNotExist:
        return False

    new_file = instance.cv
    if not old_file == new_file:
        try:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
        except ValueError:
            return False