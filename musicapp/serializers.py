from dataclasses import fields
from rest_framework import serializers
from .models import Artiste, Lyric, Song

class ArtisteSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Artiste
        fields = '__all__'


class LyricSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Lyric
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Song
        fields = '__all__'
