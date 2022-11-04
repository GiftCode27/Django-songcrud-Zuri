from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from musicapp.models import Artiste, Lyric, Song
from musicapp.serializers import UserSerializer, SongSerializer, LyricSerializer
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response






def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Artiste.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'GET':
        snippets = Song.objects.all()
        serializer = SongSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'GET':
        snippets = Lyric.objects.all()
        serializer = LyricSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Song.objects.get(pk=pk)
        snippetLyrics = Lyric.objects.get(pk=pk)
    except Artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerializer(snippet)
        return Response(serializer.data)

    if request.method == 'GET':
        serializer = LyricSerializer(snippetLyrics)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SongSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = LyricSerializer(snippetLyrics, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)