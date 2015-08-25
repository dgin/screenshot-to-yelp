from django.db import models

class Screenshot(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField()
    address = models.CharField(null=True, blank=True, max_length=120)
    city = models.CharField(null=True, blank=True, max_length=120)
    phone = models.SmallIntegerField(null=True, blank=True)
    yelp_url = models.URLField(null=True, blank=True)