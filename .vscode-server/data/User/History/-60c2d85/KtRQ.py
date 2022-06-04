from django.urls import path
from publications.views import PublicationAPIView, PublicationUpdateAPIView
from publications.api.api import publication_list, publications_availables_all, publications_availables,  publications_made, publication_filter, publication_delete, publications_all

urlpatterns = [
     path('publication/',PublicationAPIView.as_view(), name = 'publication_create_api'),
     path('publication_update/<int:pk>/',PublicationUpdateAPIView.as_view(), name = 'publication_update_api'),
     path('list_publication/',publication_list, name = 'publication_list_api'),
     path('publications_availables_all/',publications_availables_all, name = 'publications_availables_all_api'),
     path('publications_availables/<int:pk>/',publications_availables, name = 'publications_availables'),
     path('publications_made/<int:pk>/',publications_made, name = 'publications_made'),
     path('publications_all/<int:pk>/',publications_all, name = 'publications_all'),
     path('publication_filter/<str:pk>/', publication_filter, name = 'publication_filter' ),
     path('publication_delete/<int:pk>/', publication_delete, name = 'publication_delete'),

]