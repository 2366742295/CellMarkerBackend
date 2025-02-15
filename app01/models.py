from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name="姓名", blank=False, max_length=30)