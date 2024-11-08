from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True) 
    publisher = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
