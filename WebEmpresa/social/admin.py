from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Milita").exists():
            return ( 'key', 'name')
        else:
            return ('created', 'updated')
    

admin.site.register(Link, LinkAdmin)
