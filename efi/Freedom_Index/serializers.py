from rest_framework import serializers

from .models import Freedom


class FreedomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freedom
        fields = '__all__'