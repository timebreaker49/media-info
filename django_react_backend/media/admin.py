from django.contrib import admin
from .models import Media


class MediaAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'duration', 'played_at', 'href')


admin.site.register(Media, MediaAdmin)
