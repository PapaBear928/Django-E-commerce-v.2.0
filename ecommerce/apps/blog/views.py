from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .models import Post, Category
from .forms import NewCommentForm
from django.views.generic import ListView

def blog_main(request):

    posts = Post.custom.all()

    return render(request, 'blog/blog_main.html', {'posts' : posts})

def read_post(request, post):

    post = get_object_or_404(Post, slug=post, status='published')
    comments = post.comments.filter(status=True)
    user_comment = None

    if request.method == "POST":
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(request, 'blog/read_post.html', {'post': post, 'comments': user_comment, 'comments': comments, 'comment_form': comment_form})


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }
        return content


