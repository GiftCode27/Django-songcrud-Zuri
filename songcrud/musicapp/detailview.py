from .models import Artiste, Lyric, Song
from requests import JSONDecodeError
from musicapp.serializers import LyricSerializer,UserSerializer,SongSerializer
from rest_framework import generics

class ArtistDetailAPIView(generics.RetrieveAPIView):
    try:
        queryset = Artiste.objects.all()
        serializer_class = UserSerializer
    except:
        JSONDecodeError(raise_exception=True)

artist_detail_view = ArtistDetailAPIView.as_view()


class SongDetailAPIView(generics.RetrieveAPIView):
    try:
        queryset = Song.objects.all()
        serializer_class = SongSerializer
    except:
        JSONDecodeError(raise_exception=True)

song_detail_view = SongDetailAPIView.as_view()


class LyricDetailAPIView(generics.RetrieveAPIView):
    try:
        queryset = Lyric.objects.all()
        serializer_class = LyricSerializer
    except:
        JSONDecodeError(raise_exception=True)

lyric_detail_view = LyricDetailAPIView.as_view()