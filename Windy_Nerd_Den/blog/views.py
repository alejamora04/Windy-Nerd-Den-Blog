from django.shortcuts import render, get_object_or_404
from .models import Post

# Configured View the list of published post stored in the db.
def post_list(request):
    posts = Post.published.all()
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})

# Retrieves the specified post Queried via the post ID
def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})