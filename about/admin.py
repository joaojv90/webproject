from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('names', 'position')

# Register your models here.
admin.site.register(About,AboutAdmin)