from .models import Area,Qurilish_tashkiloti,Qurilish_binosi
from rest_framework import serializers

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class Qurilish_tashkilotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qurilish_tashkiloti
        fields = '__all__'

class Qurilish_binosiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Qurilish_binosi
        fields = '__all__'

