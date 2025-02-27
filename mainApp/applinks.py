from .views import homepage
from .views import aboutuspage
from .views import loginpage
from .views import moviepage 
from .views import fetch_all_players_page
from .views import fetch_all_movies_page
from .views import fetch_one_player_page
from .views import fetch_one_movie_page
from .views import update_one_player
from .views import update_one_movie
from .views import delete_one_player
from django.urls import path

urlpatterns =  [
    path("homepage/" , homepage, name="homepage"),
    path("aboutuspage/" , aboutuspage, name="aboutuspage"),
    path("loginpage/" , loginpage, name="loginpage"),
    path("moviepage/" , moviepage, name="moviepage"),
    path("allplayerspage/" , fetch_all_players_page, name="allplayerspage"),
    path("allmoviespage/" , fetch_all_movies_page, name="allmovispage"),

    path("oneplayerpage/<int:pk>" , fetch_one_player_page, name="oneplayerpage"),
    path("onemoviepage/<int:pk>" , fetch_one_movie_page, name="onemoviepage"),
    path("update_one_player_page/<int:pk>" , update_one_player, name="updateplayerpage"),
    path("update_one_movie_page/<int:pk>" , update_one_movie, name="updatemoviepage"),
    path("delete_one_player_page/<int:pk>" , delete_one_player, name="delete_one_player")
    #Note we will be visiting eg
    #htttp//127.0.0.1
    
]
