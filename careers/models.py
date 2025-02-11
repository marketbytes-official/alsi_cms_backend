from django.db import models


class CareersBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='careers/')

    def __str__(self):
        return self.title

class CareersForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField() 
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

