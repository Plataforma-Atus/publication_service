from django.urls import path

from . import views


urlpatterns = [
   path('create_publication', views.create_publication,
        name='create_publication'),
]
