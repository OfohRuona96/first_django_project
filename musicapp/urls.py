from django.urls import path
from . import index

app_name="musicapp"
urlpatterns = [
    path('', views.index, name="index"),
]  

