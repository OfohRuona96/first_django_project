from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ArtisteViewset, LyricViewset, SongViewset

router = DefaultRouter()
router.register(r'artistes', ArtisteViewset, basename='artistes')

router = DefaultRouter()
router.register(r'lyrics', LyricViewset, basename='lyrics')

router = DefaultRouter()
router.register(r'songs', SongViewset, basename='songs')

urlpatterns = [] + router.urls

#127.0.0.1:8007/artistes
#127.0.0.1:8007/lyrics
#127.0.0.1:8007/songs

