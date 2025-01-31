from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),

    path('admin-panel/', AdminPage.as_view(), name='admin-panel'),
    path('animal', AnimalListView.as_view(), name='animal_list'),
    path('animal/showcase/', AnimalShowcaseView.as_view(), name='animal_showcase'),
    path('animal/add', AnimalCreateView.as_view(), name='animal_create'),
    path('animal/<int:pk>', AnimalDetailView.as_view(), name='animal_detail'),
    path('animal/<int:pk>/update', AnimalUpdateView.as_view(), name='animal_update'),
    path('animal/<int:pk>/delete', AnimalDeleteView.as_view(), name='animal_delete'),

    path('adoption_requests/', AdoptionRequestListView.as_view(), name='adoption_request_list'),
    path('adoption_requests/add/', AdoptionRequestCreateView.as_view(), name='adoption_request_create'),
    path('adoption_requests/<int:pk>/', AdoptionRequestDetailView.as_view(), name='adoption_request_detail'),
    path('adoption_requests/<int:pk>/update/', AdoptionRequestUpdateView.as_view(), name='adoption_request_update'),
    path('adoption_requests/<int:pk>/delete/', AdoptionRequestDeleteView.as_view(), name='adoption_request_delete'),

    path('shelters/', ShelterListView.as_view(), name='shelter-list'),
    path('shelters/<int:pk>/', ShelterDetailView.as_view(), name='shelter-detail'),
    path('shelters/add/', ShelterCreateView.as_view(), name='shelter-add'),
    path('shelters/<int:pk>/edit/', ShelterUpdateView.as_view(), name='shelter-edit'),
    path('shelters/<int:pk>/delete/', ShelterDeleteView.as_view(), name='shelter-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)