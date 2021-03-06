from django.shortcuts import render, get_object_or_404

from .models import Post, Group

def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request,slug):
    group = get_object_or_404(Group, slug = slug)
    posts = group.posts.all()[:12] #код group.posts запустить не удаётся, причину не могу найти второй день
    return render(request, "group.html", {"group":group, "posts":posts})