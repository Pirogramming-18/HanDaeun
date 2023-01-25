from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    
    context = {
        "posts":posts
    }
    return render(request, template_name="posts/home.html", context=context)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)     # {id: 1, type: 'like'}, python에서 json으로 파싱
    post_id = req['id']     # 1
    button_type = req['type']   # 'like'

    post = Post.objects.get(id=post_id)

    post.save()

    return JsonResponse({'id': post_id, 'type': button_type})   # {id: 1, type: 'like'}
