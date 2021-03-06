from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .forms import PostForm
from django.utils.timezone import now


def get_categories():
    all = Category.objects.all()
    count = all.count() # 7
    half = count // 2 + count % 2
    first_half = all[:half]
    second_half = all[half:]
    return {"cat1": first_half, "cat2": second_half}


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


def post(request, id=None):
    post = get_object_or_404(Post, pk=id) #Post.objects.get(pk=id)
    context = {"post": post}
    context.update(get_categories())
    return render(request, "blog/post.html", context)


def category(request, id=None):
    #c = gbjects.filter(categet_object_or_404(Category, pk=id)
    #posts = Post.oory=c).order_by("-published_date")
    posts = Post.objects.filter(category__pk=id).order_by("-published_date")
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


def search(request):
    print(request.method)
    print(request.POST)

    if request.method == 'POST':
        query = request.POST['query']
        posts = Post.objects.filter(content__icontains=query).order_by("-published_date")
    else:
        posts = []

    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = now()
            post.save()

            return index(request)

    form = PostForm()
    return render(request, "blog/create.html", {"form": form})