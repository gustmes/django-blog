from django.shortcuts import render

from blog.models import Author, Post

# Create your views here.
def index(request):
    num_posts = Post.objects.count()
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        "num_posts": num_posts,
        "num_authors": num_authors,
        "num_visits": num_visits,
    }

    return render(request, 'blog/index.html', context=context)
