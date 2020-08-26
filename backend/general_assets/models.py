from django.db import models
from django.contrib.auth.models import User

class Competetion(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 300)
    img_tile = models.ImageField(default='default.jpg', upload_to='project_pics')
    positions = (("1", "First"),
                 ("2","Second"),
                 ("3","Third"),
                 ("Paticipated","Not among the top three"))
    result = models.CharField(max_length = 30, choices = positions)
    participants = models.ManyToManyField(User)
    def __str__(self):
        return str(self.name)

class home_carousel(models.Model):
    title = models.CharField(max_length =20, blank=True, default='')
    description = models.TextField(max_length= 300, blank=True, default='')
    img_tile = models.ImageField(default='default.jpg', upload_to='project_pics')

class news(models.Model):
    title = models.CharField(max_length =20, blank=True, default='')
    url = models.URLField(max_length=200, null=True, blank=True)
    short_description = models.TextField(max_length=50)
    long_descrption = models.TextField(max_length=300)
    img_tile = models.ImageField(default='default.jpg', upload_to='project_pics')
    is_latest = models.BooleanField()
