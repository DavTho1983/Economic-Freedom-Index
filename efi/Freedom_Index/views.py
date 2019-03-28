from django.views.generic import ListView

from .models import Freedom

class FreedomListView(ListView):
    model = Freedom
    template_name = 'freedom_list.html'



