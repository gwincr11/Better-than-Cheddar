from django.db import models

# Create your models here.
class blogRoll(models.Model):
	url  = models.URLField(blank=True,null=True)
	title = models.CharField(max_length=255,blank=True,null=True)