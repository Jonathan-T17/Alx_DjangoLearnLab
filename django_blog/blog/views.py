from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from .forms import UserRegisterForm, UserUpdateForm
from .models import Post, Comment


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Post, Comment, Tag
from django.db.models import Q
from .forms import PostForm, CommentForm


class UserLoginView(LoginView):
    template_name = "blog/login.html"


from django.contrib.auth.views import LogoutView

class UserLogoutView(LogoutView):
    template_name = "blog/logout.html"
    next_page = "blog:login"
    http_method_names = ["get", "post", "head"]  # allow GET



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect("blog:profile")
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})



def base(request):
    # Fetch latest posts (you can adjust ordering/limit)
    posts = Post.objects.order_by('-published_date')[:5]
    return render(request, "blog/base.html", {"posts": posts})



@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("blog:base")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})





class SearchResultsView(ListView):
    model = Post
    template_name = "blog/search_results.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        return Post.objects.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(tags__name__icontains=query)
            | Q(author__username__icontains=query)   # search by author username
        ).distinct()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["query"] = self.request.GET.get("q", "")
        return ctx




class TagPostListView(ListView):
    model = Post
    template_name = "blog/tag_posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        tag_name = self.kwargs["tag_name"]
        return Post.objects.filter(tags__name__iexact=tag_name)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["tag_name"] = self.kwargs["tag_name"]
        return ctx
    



# ListView - public
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # template
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5  # optional pagination


    

# DetailView - public
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Provide a blank form for posting new comments
        context['comment_form'] = CommentForm()
        return context
    
    

# CreateView - requires login
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    # after successful creation, Post.get_absolute_url will be used

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView - only author can update
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

# DeleteView - only author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    

    

# Comment create (class-based view)
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            # Redirect to post detail with anchor to new comment
            return HttpResponseRedirect(
                reverse('blog:post_detail', args=[post.pk]) + f"#comment-{comment.pk}"
            )
        # If invalid, just redirect back to post detail
        return redirect('blog:post_detail', pk=post.pk)

    def get(self, request, post_pk):
        # On GET, redirect to post detail (form is shown there)
        return redirect('blog:post_detail', pk=post_pk)



# Comment update (class-based)
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.object.post.pk]) + f"#comment-{self.object.pk}"

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user


# Comment delete (class-based)
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.object.post.pk])

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
