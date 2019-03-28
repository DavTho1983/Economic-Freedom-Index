from rest_framework import serializers

from Freedom_Index.models import Freedom


class FreedomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freedom
        fields = '__all__'