from django.db import models
from django.contrib.auth.models import User


class DiscordUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discord_id = models.CharField(max_length=20)


class Level(models.Model):
    title = models.CharField(max_length=50)
    form_link = models.URLField(max_length=200)
    response_link = models.URLField(max_length=200)
    description = models.TextField(max_length=300, blank=True, default='')
    level_number = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Levels'


class Department(models.Model):
    name = models.CharField(max_length=30)
    coordinators = models.ManyToManyField(User, related_name='corr')
    levels = models.ManyToManyField(Level, related_name='levels')

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Submission(models.Model):
    STATUS_CHOICES = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Stutus', default='Pending')
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'
