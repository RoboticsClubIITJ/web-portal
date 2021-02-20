from django.contrib import admin
from .models import Competition, Team, Position, \
    Announcement, Submission_category, Submission_teams
from django.http import HttpResponse


def download_csv(modeladmin, request, queryset):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=download.csv'

    writer = csv.writer(response)
    writer.writerow(["code", "name", "members"])
    for s in queryset:
        t = " ".join([p.email for p in s.members.all()])
        writer.writerow([str(s.code), s.name, t])
    return response


class TeamAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'team_mates')
    actions = [download_csv]

    def team_mates(self, obj):
        return "\n".join([p.email for p in obj.members.all()])


admin.site.register(Competition)
admin.site.register(Team, TeamAdmin)
admin.site.register(Announcement)
admin.site.register(Submission_category)
admin.site.register(Position)
admin.site.register(Submission_teams)
