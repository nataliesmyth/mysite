# Create your views here.

# A Django view is just a Python function that receives a web request and returns a web response. We’re going to use class-based views then map URLs for each view and create an HTML templated for the data returned from the views.

from django.shortcuts import render

from django.views import generic
from .models import Post

# The built-in ListViews which is a subclass of generic class-based-views render a list with the objects of the specified model we just need to mention the template, similarly DetailView provides a detailed view for a given object of the model at the provided template.

# Note that for PostList view we have applied a filter so that only the post with status published be shown at the front end of our blog. Also in the same query, we have arranged all the posts by their creation date. The ( – ) sign before the created_on signifies the latest post would be at the top and so on.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'