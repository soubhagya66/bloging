from django.db.models import Avg, Max, Min
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.views import View
from .forms import CommentForm
import imp
from multiprocessing import context
from time import time
from urllib.request import HTTPRedirectHandler
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from datetime import date
from.models import Post, Author, Tag


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        my_query = super().get_queryset()
        data = my_query[:3]
        return data


class AllBlogView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all__posts"



class BlogByNameView(View):

    def is_stored(self, request, post_id):

        stored_post = request.session.get("stored_post")

        if stored_post:

            saved_for_later = str(post_id) in stored_post

        else:
            saved_for_later = False

        return saved_for_later


    def get(self, request, id):
        post = Post.objects.get(pk=id)
        
        context = {
            "post": post,
            "post_tag": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later":self.is_stored(request,post.id)
        }
        print(self.is_stored(request,post.id))
        print("heloooooooooooooooooooooooooooooo")
        return render(request, "blog/post-detail.html", context)

    def post(self, request, id):
        post = Post.objects.get(pk=id)
        comment_form = CommentForm(request.POST)

        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog_by_name", args=[id]))
        


        context = {
            "post": post,
            "post_tag": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later":self.is_stored(request,post.id)
        }
        return render(request, "blog/post-detail.html", context)




class ReadLaterView(View):
    def get(self, request):
        stored_post = request.session.get("stored_post")
        context = {}
        if stored_post is None:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_post)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-post.html", context)

    def post(self, request):
        stored_post = request.session.get("stored_post")

        if stored_post is None:
            stored_post = []

        post_id = request.POST["post_id"]

        if post_id not in stored_post:
            stored_post.append(post_id)

        else:
            stored_post.remove(post_id)

        request.session["stored_post"] = stored_post
        return HttpResponseRedirect("/")
