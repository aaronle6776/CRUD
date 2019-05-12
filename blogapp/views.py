from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def new(request):
    return render(request, 'new.html')

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def create(request):
    blog=Blog()
    blog.title= request.GET['title']
    blog.writer = request.GET['writer']
    blog.pub_date = timezone.datetime.now()
    blog.body = request.GET['content']
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, delete_blog_id):
    delete_blog = get_object_or_404(Blog, pk=delete_blog_id)
    delete_blog.delete()
    return redirect('home')

def edit(request, edit_blog_id):
    edit_blog = get_object_or_404(Blog, pk=edit_blog_id)
    return render(request, 'edit.html', {'blog': edit_blog})

def update(request, update_blog_id):
    update_blog = get_object_or_404(Blog, pk= update_blog_id)
    update_blog.title = request.GET["title"]
    update_blog.writer = request.GET['writer']
    update_blog.body = request.GET['content']
    update_blog.save()
    return redirect('/blog/'+str(update_blog.id))