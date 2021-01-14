from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    team_name = models.CharField(max_length=20)
    project = models.URLField(max_length=200)


class Announcement(models.Model):
    text = models.CharField(max_length=200)
    url = models.URLField(max_length=200, blank=True, null=True)


class Submission_category(models.Model):
    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=200, blank=True, null=True)
    is_open = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, auto_now_add=False)


class Submission_teams(models.Model):
    category = models.ForeignKey(Submission_category, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)


class Competition(models.Model):
    STATUS_CHOICES = (('Active', 'Active'),
                      ('Completed', 'Completed'))
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    registration_active = models.BooleanField(default=False)
    img_tile = models.ImageField(default='default.jpg', upload_to='competition_tiles')
    description = models.TextField(max_length=300, blank=True, default='')
    rule_book = models.URLField(max_length=200)
    start = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False)
    max_team = models.IntegerField(default=1)
    submissions_category = models.ManyToManyField(Submission_category, blank=True)
    announcement = models.ManyToManyField(Announcement, blank=True)
    postion_1 = models.OneToOneField(Position, blank=True, null=True,
                                     on_delete=models.CASCADE, related_name="p1")
    postion_2 = models.OneToOneField(Position, blank=True, null=True,
                                     on_delete=models.CASCADE, related_name="p2")
    postion_3 = models.OneToOneField(Position, blank=True, null=True,
                                     on_delete=models.CASCADE, related_name="p3")

    class Meta:
        verbose_name_plural = 'Competitions'


class Team(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    members = models.ManyToManyField(User, related_name='members')
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    submissions = models.ManyToManyField(Submission_teams, blank=True)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
