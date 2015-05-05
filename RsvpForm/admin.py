from django.contrib import admin
from .models import Rsvp


class RsvpAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rsvp, RsvpAdmin)
