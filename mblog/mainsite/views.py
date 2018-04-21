from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Post
from .models import Contact

# Create your views here.

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contact.html', {'contact': contact})
