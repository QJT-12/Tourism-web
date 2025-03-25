from django.urls import path
from .views import homepage
from .views import signinpage
from .views import signup
from .views import signout
from .views import destinations



urlpatterns = [
    path("" , homepage, name="homepage"),
    path("signinpage/" , signinpage, name="signinpage"),
    path("signup/" , signup, name="signup"),
    path("signout/", signout, name="signout")
    path("destinations/" , destinations, name="destinationspage")
]
