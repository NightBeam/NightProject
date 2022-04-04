from django.contrib import admin
from .models import *

class InfaAboutUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateOfCreation', 'id')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')


class VideoOurWorksAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateOfCreation', 'id')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')

class ProgramsInfaAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateOfCreation', 'id')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')

class WeAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')

class TypeOfModelingAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')

class AnswersTableAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')

class ProgramsForBotAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')

class ProgramSettingsAdmin(admin.ModelAdmin):
    list_display = ('forWho','id')
    list_display_links = ('forWho', 'id')
    search_fields = ('forWho', 'id')


admin.site.register(InfaAboutUs, InfaAboutUsAdmin)
admin.site.register(VideoOurWorks, VideoOurWorksAdmin)
admin.site.register(ProgramsInfa, ProgramsInfaAdmin)
admin.site.register(We, WeAdmin)
admin.site.register(TypeOfModeling, TypeOfModelingAdmin)
admin.site.register(AnswersTable, AnswersTableAdmin)
admin.site.register(ProgramsForBot,ProgramsForBotAdmin)
admin.site.register(ProgramSettings,ProgramSettingsAdmin)