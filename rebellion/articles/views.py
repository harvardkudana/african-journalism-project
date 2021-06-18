from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from rebellion.articles.models import Post

class IndexView(ListView):
    model = Post
    template_name = 'index.html'

# Articles View
def index (request):
    return HttpResponse("This is the articles index")

def individual_post(request):
    return HttpResponse("This is where an individual post will be")


