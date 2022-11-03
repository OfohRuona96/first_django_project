from rest_framework import serializers
from .models import Post

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        