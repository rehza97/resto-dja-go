from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField( upload_to='food/' )
    ingrdt = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10 , decimal_places=2)
    # tp = 
    def __str__(self) -> str:
        return self.name