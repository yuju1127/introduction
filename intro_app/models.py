from django.db import models

# Create your models here.
class form(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name
