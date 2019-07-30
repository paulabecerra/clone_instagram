#Posts views.#

#Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post

#Utilities
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ListPosts(ListView):
    template_name = "posts/feed.html"
    def get(self, request):
        posts = Post.objects.all().order_by('-created')
        return render(request, self.template_name, {'posts': posts})

@method_decorator(login_required, name='dispatch')
class CreatePost(TemplateView):
    template_name = "posts/create_post.html"
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    def get(self, request):
        form = PostForm()
        return render(
            request=request,
            template_name='posts/create_post.html',
            context={
                'form': form,
                'user': request.user,
                'profile': request.user.profile
            }
        )
