from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=256)
    done = models.BooleanField(default=False)