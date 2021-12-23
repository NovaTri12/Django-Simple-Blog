from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from src import models

def home(request):
    return render(request, 'blog/index.html', {
        'title' : 'Blog Azis',
        'content' : models.Post.objects.all()
    })

def detail(request, id):
    try:
        model = models.Post.objects.get(id=id)
    except Exception:
        raise Http404()
    return render(request, 'blog/detail.html', {
        'title' : model.title,
        'model' : model
    })