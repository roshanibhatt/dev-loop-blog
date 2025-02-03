from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from blog.models import Contact


# Create your views here.
def home(request):
    return render(request,'index.html')

def blog(request):
    blogs=Blog.objects.all()
    context={'blogs':blogs}
    return render(request,'bloghome.html',context)

def contact(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        instance=Contact(name=name,email=email,phone=phone,desc=desc)
        instance.save()

    return render(request,'contact.html')

def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render(request,'blogpost.html',context)

def search(request):
    query=request.GET['query']
    blogs=Blog.objects.filter(title__icontains=query)
    params={'blogs':blogs}
    return render(request,'search.html',params)

