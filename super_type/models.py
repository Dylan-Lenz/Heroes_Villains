from django.db import models

class Super_type(models.Model):
    type = models.CharField(max_length=255)