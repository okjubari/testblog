from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post/detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #쿼리셋 
    return render(request, 'blog/post_list.html', {'posts':posts})  #쿼리셋 posts 전달 방법 



# Create your views here.

