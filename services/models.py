from django.db import models

class ServicesTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=255)
    service_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/')
    subtitle = models.CharField(max_length=2000)
    link_url = models.CharField(max_length=255)
    banner_image = models.ImageField(upload_to='services/')
    content_paragraphs = models.TextField()

    def __str__(self):
        return self.title
    
# class SubServices(models.Model):
#     service = models.ForeignKey(Services, related_name='sub_services', on_delete=models.CASCADE)
#     subservice_title = models.CharField(max_length=500)

#     def __str__(self):
#         return self.subservice_title

# class SubServicesCategory(models.Model):
#     service = models.ForeignKey(Services, related_name='sub_services_categories', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='services/')
#     title = models.CharField(max_length=500)

#     def __str__(self):
#         return self.title