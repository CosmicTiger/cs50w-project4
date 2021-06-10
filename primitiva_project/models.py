from django.utils import timezone
from django.db import models

class DateRegister(models.Model):
    created_at = models.DateTimeField(editable = False, blank = False)
    updated_at = models.DateTimeField(editable = True, blank = True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super(DateRegister, self).save(*args, **kwargs)

    class Meta:
        abstract = True
