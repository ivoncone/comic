from django.urls import path

from users import views
from users.views import CreateUserView, LoginView, UserView

urlpatterns = [
	path('users/', views.UserView.as_view()),
	path('login/', views.LoginView.as_view()),
	path('register/', views.CreateUserView.as_view())
]