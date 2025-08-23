from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RegisterForm, UserUpdateForm, ProfileForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from django.contrib.auth import login
from .models import Post, Comment, Tag
from django.db.models import Q


def home(request):
    return render(request, "blog/home.html")


# Registration View
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("blog:profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


# Login View (Django’s built-in)
class CustomLoginView(LoginView):
    template_name = "blog/login.html"


# Logout View (Django’s built-in)
class CustomLogoutView(LogoutView):
    template_name = "blog/logout.html"


# Profile View
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("blog:profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    return render(request, "blog/profile.html", {"u_form": u_form, "p_form": p_form})


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # only author can edit
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        # only author can delete
        return self.request.user == post.author


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all().order_by("-created_at")
        context["comments"] = comments
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """Handle new comment submission."""
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect("blog:post_detail", pk=self.object.pk)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


@method_decorator(login_required, name="dispatch")
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.kwargs["pk"]
        context["title"] = "Add Comment"
        return context

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.kwargs["pk"]})


@method_decorator(login_required, name="dispatch")
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_id"] = self.object.post.pk
        context["title"] = "Edit Comment"
        return context

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


@method_decorator(login_required, name="dispatch")
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


def search_posts(request):
    query = request.GET.get("q", "")
    results = Post.objects.none()

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(tags__name__icontains=query)
        ).distinct()

    return render(
        request, "blog/search_results.html", {"results": results, "query": query}
    )


def PostByTagListView(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = tag.posts.all()  # Using the related_name in the Post model
    return render(
        request, "blog/posts_by_tag.html", {"posts": posts, "tag_name": tag.name}
    )
