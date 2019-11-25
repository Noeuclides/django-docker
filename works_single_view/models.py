from django.db import models

# Create your models here.

class song(models.Model):
    """song information database class
    """
    title = models.CharField(max_length=127)
    contributors= models.CharField(max_length=127)
    iswc = models.CharField(max_length=50)
