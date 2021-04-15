from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tasks', views.CRUD.show_tasks, name='tasks'),
]
