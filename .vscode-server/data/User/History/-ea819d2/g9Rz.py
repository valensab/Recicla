from django.contrib import admin

from requests.models import Request

# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    model = Request
    list_display = ['id_request', 'publication_id', 'publication_id__user','recycler', 'state', 'is_active']

admin.site.register(Request,RequestAdmin )
