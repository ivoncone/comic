from django.urls import path

from comics import views
from comics.views import MarvelSearchView, CreateComicCollection, RetrieveComicCollection

urlpatterns = [
	path('searchComics/', MarvelSearchView.as_view()),
	path('addToLayaway/', CreateComicCollection.as_view()),
	path('getLayawayList/', RetrieveComicCollection.as_view()),
]