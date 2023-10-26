from django.shortcuts import render
from blog.models import Post
from math import ceil
from django.shortcuts import render


def blogHome(request): 

    allProds = []
    catprods = Post.objects.values('category', 'sno')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Post.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])


    params = {'allProds': allProds}
    return render(request, 'blog/blogHome.html', params)

def blogPost(request, slug): 

    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogPost.html", context)



