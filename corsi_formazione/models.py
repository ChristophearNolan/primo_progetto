from django.db import models

# Create your models here.
class corso(models.Model):
     titolo = models.CharField(max_length=100)
     descrizione = models.TextField()
     data_inizio= models.DateField(blank=True)
     data_fine=models.DateField(blank=True)
     posti_disponibili=models.IntegerField(default=0,blank=True)
