from django.urls import path
from requests.views import RequestAPIView
from requests.api.api import publication_list

urlpatterns = [
     path('add_request/',RequestAPIView.as_view(), name = 'requests_create_api'),
     path('list_request/',request_list, name = 'requests_list_api'),
]