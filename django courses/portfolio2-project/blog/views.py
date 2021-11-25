from django.shortcuts import render, get_object_or_404
from blog.models import Blog

# Create your views here.
def allbolgs(request):
    blog=Blog.objects
    context={"blogs":blog}
    return render (request,'blog/allblogs.html',context)

def detail(request,blog_id):
    detailBlog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':detailBlog})
