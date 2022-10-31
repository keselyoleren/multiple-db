from cgitb import reset
from errno import EILSEQ
from django.shortcuts import get_object_or_404, render
from matplotlib.pyplot import get
from rest_framework import (
    status,
    generics,
    viewsets,
    permissions,
    views,
    response,
)
from yaml import serialize
from penduduk.models import Warga
from itertools import chain

from penduduk.serialize import WargaSerialize
# Create your views here.

class WargaViewSet(generics.CreateAPIView, generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView, viewsets.ModelViewSet):
    serializer_class = WargaSerialize
    queryset = Warga.objects.all()
    
    def list(self, request, *args, **kwargs):
        data = list(chain(Warga.objects.using('db_us'), self.queryset))
        serialize = self.serializer_class(data, many=True)
        return response.Response(serialize.data)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if request.data['country'] == 'US':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(using='db_us')
            return response.Response(serializer.data)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.data['country'] == 'US':
            return super().update(request, *args, **kwargs).using('db_us')
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
