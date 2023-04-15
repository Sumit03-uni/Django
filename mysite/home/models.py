from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.TextField(max_length=50)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
