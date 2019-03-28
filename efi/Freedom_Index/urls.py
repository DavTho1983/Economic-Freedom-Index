from django.urls import path
# from rest_framework import routers

from .views import FreedomListView

# router = routers.DefaultRouter()
# router.register(r'freedom', FreedomViewSet)

urlpatterns = [
    path('', FreedomListView.as_view(), name='home')
]