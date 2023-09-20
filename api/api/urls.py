from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from comics.views import MarvelView
router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('comics.urls')),
    path('', include(router.urls)),
]
