from django.contrib.auth.models import User
from django.urls import path
from users.api.api import user_list, user_delete, user_count, user_change_password
from users.views import RegisterProvider, RegisterRecycler, Login, Logout

urlpatterns = [
    path('list/',user_list, name = 'user_list_api'),
    path('count/',user_count, name = 'user_count_api'),
    path('provider/',RegisterProvider.as_view(), name = 'register_provider_api'),
    path('recycler/',RegisterRecycler.as_view(), name = 'register_recycler_api'),
    path('delete/<int:pk>/',user_delete, name = 'user_delete_api'),
    path('login/',Login.as_view(), name = 'user_login_api'),
    path('logout/',Logout.as_view(), name = 'user_logout_api'),
    # path('validate_token/', UserToken.as_view(), name = 'usuario_validate_api' ),
    path('change_password/<int:pk>/', user_change_password, name = 'user_change_api' ),
]
