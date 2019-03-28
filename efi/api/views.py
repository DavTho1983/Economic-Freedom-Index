from rest_framework import generics

from Freedom_Index.models import Freedom
from Freedom_Index.serializers import FreedomSerializer

# Create your views here.
class FreedomAPIView(generics.ListAPIView):
    queryset = Freedom.objects.all()
    serializer_class = FreedomSerializer
