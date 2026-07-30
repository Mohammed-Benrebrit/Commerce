from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("creat", views.creat, name="creat"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing", views.listings, name="listing"),
    path("my_listing", views.my_listing, name="my_listing"),
    path("salles", views.salles, name="salles")


]
