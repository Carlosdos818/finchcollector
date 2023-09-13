from django.db import models
# need the reverse method from django urls fro redirects
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    habitat = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    # this is used to redirects from class based views
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})