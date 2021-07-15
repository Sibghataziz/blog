from django.shortcuts import render,redirect
from .form import Add_Post,Add_Comment
from django.contrib import messages
from .models import Post,Comment

# Create your views here.
def post_view(request):
    if request.method == 'POST':
        body =request.POST.get("body")
        # image =request.POST.get("image")
        auth=request.user
        new_post=Post(body=body,author=auth)
        new_post.save()
        return redirect('home')
    else:
        new_post=Add_Post
    return render(request,'post/Add_post.html',{'form':new_post})

def home_view(request):
    posts=Post.objects.all()
    ordering=['post_date']
    return render(request,'post/home.html',{'posts':posts})

def post_detail_view(request, id):
    obj = Post.objects.get(id=id)
    context = {
        "object": obj,
    }
    return render(request, "post/post_detail.html", context)

def delete_post_view(request,id=None):
    obj=Post.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        # print("sub jhol hai")
        return redirect('home')
    context = {
        'object': obj
    }
    return render(request,'post/post_delete.html',context)

def add_comment_view(request,id):
    if request.method == 'POST':
        #print(request.POST.get("body"))
        #print(request.POST.get("image"))
        body =request.POST.get("body")
        # image =request.POST.get("image")
        post=Post.objects.get(id=id)
        auth=request.user
        comment= Comment(body=body,post=post,author=auth)
        comment.save()
        return redirect(f"home")
    else:
        new_comment=Add_Comment
    return render(request,'post/add_comment.html',{'form':new_comment})
