from django.urls import path
from .views import FreedomAPIView

urlpatterns = [
    path('', FreedomAPIView.as_view(), name='freedom_api'),
]