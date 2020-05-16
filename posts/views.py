from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import *


@login_required(login_url='/login/',redirect_field_name=None)
def create_post(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('description')
        Post.objects.create(title=title, body=body, author=user)
    
    context = {}
    return render(request,'posts/create_post.html', context)

@login_required(login_url='/login/')
def post_view(request):
    # all_posts = Post.objects.all()
    user = request.user
    all_friends = user.friendlist_set.all() | user.profile2.all()
    # new_posts = None
    new_posts = ''
    for i in all_friends:
        new_posts = i.profile1.author.all() | i.profile2.author.all()
    # new_posts=Post.objects.all().first()

    # for i in all_friends:
    #     for j in i.profile1.author.all():
    #         new_posts = new_posts['post'].append(j)
    # for i in all_friends:
    #     for j in i.profile2.author.all():
    #         new_posts = new_posts['post'].append(j)


    print('other',new_posts)
    try:
        new_posts = new_posts | user.author.all()
    except:
        new_posts=user.author.all()
    print('my',new_posts)


    context = {
        'all_posts' : new_posts,
        'user' : user
    }

    return render(request, 'posts/posts_list.html', context)

@login_required(login_url='/login/')
def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('id')  
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect('posts:post_list')

