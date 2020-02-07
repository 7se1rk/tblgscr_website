from django.shortcuts import render
from django.utils import timezone
from .models import Post

def home(request):
    return HttpResponse('<h1>hello world</h1>')

def login(request):
    return render(request, 'html/login.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'html/post_list.html', {'posts':posts})

