from django.shortcuts import render, redirect
from .models import Post

def home(request):
    posts = Post.objects.all()
    
    context = {
        "posts":posts
    }
    return render(request, template_name="posts/home.html", context=context)

def create(request):
    if request.method == 'POST':
        title = request.POST["title"]
        year = request.POST["year"]
        actor = request.POST["actor"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        review = request.POST["review"]
        director = request.POST["director"]
        running = request.POST["running"]

        Post.objects.create(title=title, year=year, actor=actor, genre=genre, star=star, review=review, director=director, running=running)
        return redirect("/")

    context = {}

    return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request, template_name="posts/detail.html", context=context)

def update(request, id):
    if request.method == 'POST':
        title = request.POST["title"]
        year = request.POST["year"]
        actor = request.POST["actor"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        review = request.POST["review"]
        director = request.POST["director"]
        running = request.POST["running"]

        Post.objects.filter(id=id).update(title=title, year=year, actor=actor, genre=genre, star=star, review=review, director=director, running=running)
        return redirect(f"/post/{id}")
    
    post = Post.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request, template_name="posts/update.html", context=context)

def delete(request, id):
    Post.objects.filter(id=id).delete()
    return redirect("/")