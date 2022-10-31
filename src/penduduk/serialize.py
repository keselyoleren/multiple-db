from rest_framework import serializers

from penduduk.models import Warga

class WargaSerialize(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = "__all__"
