from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Player
from .models import Movie
# Create your views here.
def homepage ( request ):
    return HttpResponse("hello from python")

def aboutuspage ( request ):
    return HttpResponse("<h1>My email is g@mail.com<h1>")

def moviepage ( request ):
    print("you did a " + request.method)
    if request.method == "POST":
        print( request.POST ) #new 
        moviename = request.POST.get ("moviename")
        print("The movie you typed is: "+ moviename)#new
        moviedescription = request.POST.get ("moviedescription")
        print("The description you typed is: " + moviedescription)#new
        new_movie = Movie(name=moviename, description=moviedescription)#new
        new_movie.save()
    return render(request, "movie.html")


def loginpage ( request ):
    print("you did a " + request.method)
    if request.method == "POST":
        print( request.POST ) #new 
        typedname = request.POST.get ("username")
        print("The name you typed is: "+ typedname)#new
        typedpassword = request.POST.get ("password")
        print("The password you typed is: " + typedpassword)#new
        new_player = Player(username=typedname, password=typedpassword)#new
        new_player.save()
    return render(request, "login.html")

#a page to read/show all users
def fetch_all_players_page(request):
    all_players = Player.objects.all()
    return render(request, "all_players.html",{"all_players"  :all_players})

def fetch_all_movies_page(request):
    all_movies = Movie.objects.all()
    return render(request, "all_movies.html",{"all_movies"  :all_movies})

def fetch_one_player_page(request , pk): #which player 1, 46, 38
    single_player = Player.objects.get(pk = pk)#get the layer from db
    return render(request, "oneplayer.html", {"single_player":single_player})

def fetch_one_movie_page(request , pk):
    single_movie = Movie.objects.get(pk = pk)
    return render(request, "onemovie.html", {"single_movie":single_movie})
    #TODO - fecth the movie form pk and show it on 
    #a html file


def update_one_player(request , pk):
    single_player = Player.objects.get(pk=pk)
    #if they clicked on a button
    if request.method == "POST":
        new_username = request.POST.get("username")
        print(new_username)
        new_password = request.POST.get("password")
        single_player.username = new_username
        single_player.password = new_password
        single_player.save()

    return render(request, "update_one_player.html" , {"single_player":single_player})

def update_one_movie(request , pk):
    single_movie = Movie.objects.get(pk = pk)
    return render(request, "update_one_movie.html", {"single_movie":single_movie})

def delete_one_player(request , pk):
    single_player = Player.objects.get(pk=pk)
    single_player.delete()
    return redirect("homepage")
 

    #TODO FETCH ALL MOIVES FROM MOVIES TABLE &
    #RETURN A HTML SHOWING All MOVIES



# {"english" : 40 } #this is dictionary