from django.db import models


class insertProduct(models.Model):
    name = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=500,blank=False)
    slug = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
      
        return self.name
