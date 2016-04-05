from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from .models import Post # From current directory /models.py import Post model

# Create your views here.

def post_list(request):
	# We want published blog posts sorted by published_date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'my_blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'my_blog/post_detail.html', {'post': post})
