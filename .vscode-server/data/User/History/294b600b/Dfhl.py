from django.contrib import admin

from publications.models import Publication

# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id','name','last_name','is_active','is_provider', 'is_recycler','is_staff','is_superuser')
admin.site.register(Publication)
