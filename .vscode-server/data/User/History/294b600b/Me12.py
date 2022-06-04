from django.contrib import admin
from publications.models import Publication

# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['id_publication', 'user', 'state']


admin.site.register(Publication, PublicationAdmin)
