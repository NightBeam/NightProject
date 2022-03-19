from django.contrib import admin
from .models import *

class InfaAboutUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateOfCreation', 'id')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')


class ImagesOurWorksAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateOfCreation', 'id')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')


admin.site.register(InfaAboutUs, InfaAboutUsAdmin)
admin.site.register(ImagesOurWorks, ImagesOurWorksAdmin)