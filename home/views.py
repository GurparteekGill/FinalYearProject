
from django.shortcuts import render
from home.models import Contact
from blog.models import Post
from django.contrib import messages

def home(request): 
    blogs= Post.objects.order_by("-timeStamp")[:6]
    print(blogs)
    return render(request,'home/home.html',{'blogs':blogs})

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def about(request): 
   return render(request,'home/about.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsOverview =Post.objects.filter(overview__icontains=query)
        allPostcategory =Post.objects.filter(category__icontains=query)
        allPosts=  allPostsTitle.union(allPostsOverview,allPostcategory)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

