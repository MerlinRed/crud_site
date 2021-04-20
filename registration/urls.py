from django.urls import path

from . import views

urlpatterns = [
    path('', views.RegistrationNewUser.as_view(), name='registration'),
    path('auth', views.AuthUser.as_view(), name='authorization'),
    path('exit', views.ExitFromSite.as_view(), name='exit'),
]
