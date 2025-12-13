from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from django.core.mail import send_mail          # ✅ NEW
from django.conf import settings                # ✅ NEW

from .models import Post
from .forms import SignUpForm, PostForm


def home(request):
    """
    Home page: list all published posts.
    Supports search with ?q=...
    """
    query = request.GET.get("q", "")

    posts = Post.objects.filter(published=True)
    if query:
        posts = posts.filter(title__icontains=query)

    context = {
        "posts": posts,
        "query": query,
    }
    return render(request, "blog/home.html", context)


def post_detail(request, slug):
    """
    Show single post page.
    """
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, "blog/post_detail.html", {"post": post})


@login_required
def post_create(request):
    """
    Create a new post (only for logged-in users).
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully.")
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm()

    return render(
        request,
        "blog/post_form.html",
        {"form": form, "page_title": "Create Post"},
    )


@login_required
def post_edit(request, slug):
    """
    Edit an existing post (only by its author).
    """
    post = get_object_or_404(Post, slug=slug, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "blog/post_form.html",
        {"form": form, "page_title": "Edit Post"},
    )


def signup_view(request):
    """
    Register a new user and log them in.
    Also sends a welcome email to the registered email.
    """
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created. Welcome!")

            # ✅ SEND WELCOME EMAIL (only if user has email)
            if user.email:
                subject = "Welcome to ProBlog!"
                message = (
                    f"Hi {user.username},\n\n"
                    "Thank you for registering on ProBlog.\n"
                    "You can now create, edit, and share your blog posts.\n\n"
                    "Happy blogging!\n"
                    "- ProBlog Team"
                )

                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=True,   # change to False if you want to see errors
                )

            return redirect("home")
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    """
    Log in existing user.
    """
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    """
    Log out and go back to home.
    """
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")
