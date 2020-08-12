from django.db import models


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
    name = models.CharField(max_length=60)
    position = models.CharField(max_length=20, choices=POSITION)
    techstack = models.ManyToManyField(TechStack)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    member_image = models.ImageField(default='default_member.png', upload_to='member_pics')

    def __str__(self):
        return self.name
