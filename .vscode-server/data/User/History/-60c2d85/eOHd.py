from django.urls import path
from publications.views import PublicationAPIView
from publications.api.api import publication_list, publications_availables, publications_made, publication_filter

urlpatterns = [
     path('publication/',PublicationAPIView.as_view(), name = 'publication_create_api'),
     path('publication_update/<int:pk>/',PublicationUpdateAPIView.as_view(), name = 'publication_update_api'),
     path('list_publication/',publication_list, name = 'publication_list_api'),
     path('publications_availables/<int:pk>/',publications_availables, name = 'publications_availables'),
     path('publications_made/<int:pk>/',publications_made, name = 'publications_made'),
     path('publication_filter/<str:pk>/', publication_filter, name = 'publication_filter' ),
]