from django.contrib import admin
from users.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','last_name','email','is_active','is_provider', 'is_recycler','is_staff','is_superuser')


admin.site.register(User, UserAdmin)
