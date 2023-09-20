from django.urls import path

from comics import views
from comics.views import MarvelSearchView

urlpatterns = [
	path('searchComics/', MarvelSearchView.as_view()),
]