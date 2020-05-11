from django.db import models

# Create your models here.
class Cake(models.Model):
    cake_name = models.CharField(max_length=9)
    cake_info = models.TextField(max_length=20, null=True, blank=True)
    cake_image = models.ImageField(blank=False)
    
    def __str__(self):
        return self.cake_name

