from django.db import models

# Create your models here.
class musicalWork(models.Model):
    """musical work information database class
    """
    title = models.CharField(max_length=127)
    contributors= models.CharField(max_length=127)
    iswc = models.CharField(max_length=50)

    
