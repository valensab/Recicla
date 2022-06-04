from django.contrib import admin

from requests.models import Request

# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    model = Request
    list_display = ['id_request', 'publication_id', 'get_name','recycler', 'state', 'is_active']
    
    def get_name(self, obj):
        return obj.publication.user_id

admin.site.register(Request,RequestAdmin )
