from django.db import models

class ContactBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='contact/')

    def __str__(self):
        return self.title

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField() 

    def __str__(self):
        return self.name
