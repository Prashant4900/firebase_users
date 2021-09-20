from rest_framework import generics
from .models import DummyModel
from .serializer import DummySerializer
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json


class MusicianListView(generics.ListCreateAPIView):
    queryset = DummyModel.objects.all()
    serializer_class = DummySerializer

    def aaa(self):
        print(json.dumps(self.serializer_class))


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DummySerializer
    queryset = DummyModel.objects.all()


class AlbumListView(generics.ListCreateAPIView):
    queryset = DummyModel.objects.all()
    serializer_class = DummySerializer


class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DummySerializer
    queryset = DummyModel.objects.all()
