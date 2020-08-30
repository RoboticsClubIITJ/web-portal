from django.db import models
from django.contrib.auth.models import User


class TechStack(models.Model):
    # Model
    tech_name = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Tech Stack'
        verbose_name_plural = 'Tech Stack'

    def __str__(self):
        return self.tech_name


class UserProfile(models.Model):
    PROG_CHOICES = (
        ('BT', 'B.Tech'),
        ('MT', 'M.Tech'),
        ('MSc', 'M.Sc'),
        ('PhD', 'PhD')
    )
    YEAR_CHOICES = (
        ('1', 'Freshman Year'),
        ('2', 'Sophomore Year'),
        ('3', 'Pre-final Year'),
        ('4', 'Final Year')
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender')
    )
    BRANCH_CHOICES = (
        ('CSE', 'Computer Science and Engineering'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CH', 'Chemistry'),
        ('MA', 'Mathematics'),
        ('PHY', 'Physics'),
        ('MME', 'Metallurgical and Materials Engineering'),
        ('HSS', 'Humanities and Social Sciences'),
        ('BBE', 'Bioscience and Bioengineering'),
        ('CE', 'Chemical Engineering'),
        ('CI', 'Civil Engineering'),
        ('AI', 'AI and Data Science')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    roll_number = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=10, null=True)
    prog = models.CharField(max_length=5, choices=PROG_CHOICES, verbose_name='Programme', default='BT')
    year = models.CharField(max_length=1, choices=YEAR_CHOICES, default='1')
    avatar = models.ImageField(upload_to='avatar', default='default_member.png', height_field=None, width_field=None, blank=True)
    branch = models.CharField(max_length=5, choices=BRANCH_CHOICES)
    techstack = models.ManyToManyField(TechStack, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()
