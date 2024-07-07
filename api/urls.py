

from django.urls import path
from .views import CreateUser, UserLogin, GetUser, Getorganizations, AddUserToOrganization, CreateOrganization, GetOrganization

urlpatterns = [
    path('auth/register', CreateUser),
    path('auth/login', UserLogin),
    path('api/users/<str:pk>', GetUser),
    path('api/organisations', Getorganizations),
    path('api/organisations/<uuid:org_id>', GetOrganization),
    path('api/organisations/<int:pk>/users', AddUserToOrganization),
    path('api/organisations/create', CreateOrganization),
]