from django.urls import path, include


from .views import (
    index,
    AnimeListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("anime_list", AnimeListView.as_view(), name="anime_list"),

 
]

app_name = "app_anime_list"