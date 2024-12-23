from django.db import models

class Basvuru(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=30,default='girilmedi')
    momname = models.CharField(max_length=30,default='girilmedi')
    email = models.EmailField()
    message = models.TextField()

