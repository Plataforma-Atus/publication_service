from django.contrib import admin

from publisher import models

class ListNewspaperSection(admin.ModelAdmin):
    list_display = ('name_section', 'newspaper_id')

class ListPublicationType(admin.ModelAdmin):
    list_display = ('name', 'newspaper_section_id')

admin.site.register(models.UF)
admin.site.register(models.City)
admin.site.register(models.Newspaper)
admin.site.register(models.Font)
admin.site.register(models.NewspaperSection, ListNewspaperSection)
admin.site.register(models.PublicationTypeName)
admin.site.register(models.PublicationType, ListPublicationType)
admin.site.register(models.Client)
admin.site.register(models.Publication)
