from django.shortcuts import render, redirect
from .models import Post, Tool

def posts_list(request):
    posts = Post.objects.all()
    
    context = {
        "posts":posts
    }
    return render(request, template_name="posts/posts_list.html", context=context)

def posts_create(request):
    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtool = request.POST["devtool"]
        photo = request.FILES.get("photo")
        Post.objects.create(title=title, content=content, interest=interest, devtool=devtool, photo=photo)
        page = Post.objects.last()
        return redirect(f"/posts/{page.id}")
    context = {}
    return render(request, template_name="posts/posts_create.html", context=context)

def posts_retrieve(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request, template_name="posts/posts_retrieve.html", context=context)

def posts_update(request, id):
    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtool = request.POST["devtool"]
        photo = request.FILES.get("photo")
        Post.objects.filter(id=id).update(title=title, content=content, interest=interest, devtool=devtool, photo=photo)
        return redirect(f"/posts/{id}")
    post = Post.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request, template_name="posts/posts_update.html", context=context)


def posts_delete(request, id):
    Post.objects.filter(id=id).delete()
    return redirect("/")


def tool_list(request):
    posts = Tool.objects.all()
    
    context = {
        "posts":posts
    }
    return render(request, template_name="posts/tool_list.html", context=context)

def tool_create(request):
    if request.method == 'POST':
        name = request.POST["name"]
        content = request.POST["content"]
        kind = request.POST["kind"]
        Tool.objects.create(name=name, content=content, kind=kind)
        page = Tool.objects.last()
        return redirect(f"/posts/{page.id}/tool_retrieve")
    context = {}
    return render(request, template_name="posts/tool_create.html", context=context)

def tool_retrieve(request, id):
    post = Tool.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request, template_name="posts/tool_retrieve.html", context=context)

def tool_update(request, id):
    if request.method == 'POST':
        name = request.POST["name"]
        content = request.POST["content"]
        kind = request.POST["kind"]
        Tool.objects.filter(id=id).update(name=name, content=content, kind=kind)
        return redirect(f"/posts/{id}/tool_retrieve")
    post = Tool.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request, template_name="posts/tool_update.html", context=context)

def tool_delete(request, id):
    Tool.objects.filter(id=id).delete()
    return redirect(f"/posts/tool_list")

