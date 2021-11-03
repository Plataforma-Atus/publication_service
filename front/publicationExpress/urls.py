"""publicationExpress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from publisher import views


router = routers.DefaultRouter()
router.register(r'uf', views.UFViewSet)
router.register(r'city', views.CityViewSet)
router.register(r'newspaper', views.NewspaperViewSet)
router.register(r'font', views.FontViewSet)
router.register(r'newspaper_section', views.NewspaperSectionViewSet)
router.register(r'publication_type_name', views.PublicationTypeNameViewSet)
router.register(r'publication_type', views.PublicationTypeViewSet)
router.register(r'client', views.ClientViewSet)
router.register(r'publication', views.PublicationViewSet)

urlpatterns = [
                  path('', include(router.urls)),
                  path('admin/', admin.site.urls),
                  path('api-auth/', include('rest_framework.urls')),
                  path('ajax/newspaper_section/', views.newspaper_section_dropdown, name='newspaper_section_dropdown'),
                  path('ajax/publication_type/', views.publication_type_dropdown, name='publication_type_dropdown'),
                  path('publications/', views.publications, name='publications'),
                  path('create_publication', views.create_publication, name='create_publication'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
