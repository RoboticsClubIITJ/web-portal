from django.contrib import admin
from .models import Competition, Team, Position, \
    Announcement, Submission_category, Submission_teams


admin.site.register(Competition)
admin.site.register(Team)
admin.site.register(Announcement)
admin.site.register(Submission_category)
admin.site.register(Position)
admin.site.register(Submission_teams)
