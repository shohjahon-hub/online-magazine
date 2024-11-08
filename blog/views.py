from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import post
# Create your views here.
class blogListView(ListView):
    model=post
    template_name='home.html'

class blogDetailView(DetailView):
    model=post
    template_name='post_detail.html'

    