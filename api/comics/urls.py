from django.urls import path

from comics import views
from .views.marvelView import MarvelSearchView
from .views.comicView import RetrieveComicCollection
from .views.createComic import CreateComicCollection

urlpatterns = [
	path('searchComics/', MarvelSearchView.as_view()),
	path('addToLayaway/', CreateComicCollection.as_view()),
	path('getLayawayList/', RetrieveComicCollection.as_view()),
]