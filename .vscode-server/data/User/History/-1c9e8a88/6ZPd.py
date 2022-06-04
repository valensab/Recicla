from django.urls import path
from requests.views import RequestAPIView, RequestAcceptAPIView, RejectRequestAPIView
from requests.api import request_list, requests_availables, accepted_request

urlpatterns = [
     path('add_request/',RequestAPIView.as_view(), name = 'requests_create_api'),
     path('list_request/',request_list, name = 'requests_list_api'),
     path('requests_availables/<int:pk>/',requests_availables, name = 'requests_availables_api'),
     path('reject_request/',RejectRequestAPIView.as_view(), name = 'reject_requests_api'),
     path('accepted_request/',RequestAcceptAPIView.as_view(), name = 'accepted_request_api'),
]
