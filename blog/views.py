import imp
from multiprocessing import context
from django.shortcuts import render
from . models import Post
#from django.http import HttpResponse

# posts = [
#     {
#         'author': 'Irajan',
#         'title': 'django',
#         'content': 'first page',
#         'date_posted': 'january 30, 2022'
#     },
#     {
#         'author': 'Irajan2',
#         'title': 'django2',
#         'content': 'second page',
#         'date_posted': 'january 31, 2022'
#     }
# ]

def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #render templates

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
