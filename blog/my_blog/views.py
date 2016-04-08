from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone

from .models import Post # From current directory /models.py import Post model

from .models import User

#from django.contrib.auth.models import User

# Create your views here.

def post_list(request):
	# We want published blog posts sorted by published_date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    username = request.session['username']
    if(username):
    	return render(request, 'my_blog/post_list.html', {'posts': posts, 'username': username})
    else:
    	return render(request, 'my_blog/post_list.html', {'posts': posts, 'username': ''})

def post_detail(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'my_blog/post_detail.html', {'post': post})

def post_create(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    author = User.objects.get(username='admin')

    post = Post.objects.create(author=author, title=title, text=text)
    post.publish()
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'my_blog/post_list.html', {'posts': posts})

def login(request):
    return render(request, 'my_blog/login.html')

def register(request):
	return render(request, 'my_blog/register.html')

def login_auth(request):
	email = request.POST.get('email')
	password = request.POST.get('password')
	user = User.objects.get(email=email)
	if(user):
		if(user.password == password):
			request.session['username'] = user.name
			request.session['email'] = user.email
			return redirect('/', request)
		else: 
			return redirect('/login')
	else:
		return redirect('/login')

def logout(request):
	request.session['username'] = ''
	return redirect('/', request)


