from django.contrib import admin

from requests.models import Request

# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id_request', 'publication_id', 'user_id', 'recycler', 'state']

admin.site.register(Request,RequestAdmin )
