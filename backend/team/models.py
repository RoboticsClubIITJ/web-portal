from django.db import models
from apiauth.models import UserProfile


class Member(models.Model):
    # Position
    POSITION = (
        ('Member', 'Member'),
        ('Vice-Captain', 'Vice-Captain'),
        ('Captain', 'Captain')
    )

    # Model
    member = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, choices=POSITION)

    def __str__(self):
        return self.member.user.get_full_name()
