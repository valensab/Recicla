from django.urls import path
from requests.views import RequestAPIView

urlpatterns = [
     path('add_request/',RequestAPIView.as_view(), name = 'requests_create_api'),

]