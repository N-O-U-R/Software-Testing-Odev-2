from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

def blog_list(request):
    posts = Post.objects.all().order_by('-date_posted')
    paginator = Paginator(posts, 6)  # Show 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'page_obj': page_obj})

def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    next_post = Post.objects.filter(id__gt=post_id).order_by('id').first()
    previous_post = Post.objects.filter(id__lt=post_id).order_by('-id').first()
    return render(request, 'blog-single-post.html', {
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post,
        'header_style': 'light',  # Corrected from "header-style" to "header_style"
    })

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author as the current user
            post.save()
            return redirect('blog_list')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form,})