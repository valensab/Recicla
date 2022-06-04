from django.contrib import admin

from requests.models import Request

# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    model = Request
    list_display = ['id_request', 'publication_id', 'proveedor','recycler', 'state', 'is_active']
    
    def proveedor(self, obj):
        return obj.publication.user

admin.site.register(Request,RequestAdmin )
