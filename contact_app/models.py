from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254, null=True)
    phone=models.CharField(max_length=12, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    msg=models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.name