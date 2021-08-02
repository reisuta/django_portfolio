from django.db import models
from django.utils import timezone
# Create your models here.

class Write(models.Model):
    title = models.CharField('たいとる',max_length=200)
    text = models.TextField('ほんぶん')
    date = models.DateTimeField('ひづけ',default=timezone.now)