from django.db import models

from django import forms

# Create your models here.
class contactforms(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()
    def __str__(self):
        return self.fullname
    