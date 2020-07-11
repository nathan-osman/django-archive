from django.db import models


class Sample(models.Model):
    """
    A sample model that exists for testing
    """

    attachment = models.FileField(upload_to='attachments')
