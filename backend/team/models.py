from django.db import models
from apiauth.models import UserProfile


class TechStack(models.Model):
    #Model
    tech_name = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Tech Stack'
        verbose_name_plural = 'Tech Stack'

    def __str__(self):
        return self.tech_name


class Member(models.Model):
    #Position 
    POSITION = (
        ('Member', 'Member'),
        ('Vice-Captain', 'Vice-Captain'),
        ('Captain', 'Captain')
    )

    #Model
    member = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, choices=POSITION)
    techstack = models.ManyToManyField(TechStack)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.member.user.get_full_name()
