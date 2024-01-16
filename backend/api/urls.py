from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='api_home_view'),
    path('<int:pk>', views.MovieDetails.as_view(), name='movie_details'),
    
]
