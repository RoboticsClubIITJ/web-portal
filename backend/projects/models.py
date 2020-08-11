from django.db import models


class Member(models.Model):
    #Model
    member_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.member_name


class Project(models.Model):
    #Status 
    STATUS_CHOICE = (
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    )

    #Model
    name = models.CharField(max_length=60)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    repository_link = models.URLField(max_length=200, null=True, blank=True)
    project_url = models.URLField(max_length=200, null=True, blank=True)
    img_tile = models.ImageField(default='default.jpg', upload_to='project_pics')
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self.name
