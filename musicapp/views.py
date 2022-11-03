from rest_framework.generics import viewsets
from .models import Artiste, Lyric, Song
from .serializers import ArtisteSerializer, LyricSerializer, SongSerializer


class ArtisteViewset(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class LyricViewset(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer

class SongViewset(viewsets.ModelViewSet):
    queryset = SongSerializer.objects.all()
    serializer_class = SongSerializer     