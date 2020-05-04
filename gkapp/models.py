from django.db import models

# Create your models here.
class Cake(models.Model):
    cake_info = models.CharField(max_length=100, null=True)
    cake_image = models.ImageField(blank=False)
    cake_name = models.TextField(max_length=10)

    def __str__(self):
        return self.cake_name
class PostImage(models.Model):
    post = models.ForeignKey(Cake, default=None, on_delete=models.CASCADE)
    cake_image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.post
