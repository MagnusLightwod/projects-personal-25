from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages import get_messages
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #Post.objects.all().order_by('published_date')
    #Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts}) # render html 'posts' with our posts here

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def footer(request):
    """Simple home page that links to the posts list."""
    return render(request, 'blog/home.html')

def post_page (request, slug):
    post = Post.objects.get(slug=slug) # get one post that matches slug in function
    #Post.objects.all().order_by('published_date')
    #Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'post': post})

def register_view (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = UserCreationForm()
    # need blog here has it is part of the file tree
    return render(request, 'blog/users/register.html', { 'form': form}) 

def login_view (request): 
    return 


def messages_view (request): 
    message = get_messages(request)
    return render(request, 'blog/users/messages.html', {'message': message})

# need to make a url tp an html page, 
# and display it with a view that takes in a request and does stuff