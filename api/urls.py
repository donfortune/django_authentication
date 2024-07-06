# from django.urls import path
# from .views import *
# from rest_framework.routers import DefaultRouter,APIRootView


# class CustomApiRootView(APIRootView):
#     renderer_classes = [renderers.JSONRenderer]

# class CustomRouter(DefaultRouter):
#     APIRootView = CustomApiRootView
    
# router = CustomRouter(trailing_slash=False)
# router.register('api/organisations', Getorganizations , 'organisation')

# urlpatterns = [
#     path('auth/register', CreateUser.as_view()),
#     path('auth/login',UserLogin.as_view() ),
#     path('api/users/<str:pk>', GetUser.as_view()),

# ] + router.urls

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