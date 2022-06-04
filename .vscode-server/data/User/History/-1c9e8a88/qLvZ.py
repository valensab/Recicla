from django.urls import path
from requests.views import RequestAPIView
from requests.api.api import request_list, requests_availables, reject_request, accepted_request

urlpatterns = [
     path('add_request/',RequestAPIView.as_view(), name = 'requests_create_api'),
     path('list_request/',request_list, name = 'requests_list_api'),
     path('requests_availables/<int:pk>/',requests_availables, name = 'requests_availables_api'),
     path('reject_request/<int:pk>/',reject_request, name = 'reject_requests_api'),
     path('accepted_request/<int:pk>/',accepted_request, name = 'accepted_request_api'),
]