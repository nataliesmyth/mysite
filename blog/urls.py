# Add URL patterns for Views

# We need to map the URL for the views we made above. When a user makes a request for a page on your web app, the Django controller takes over to look for the corresponding view via the urls.py file, and then return the HTML response or a 404 not found error, if not found.

from . import views
from django.urls import path

# Mapped general URL pattern from our views using the path FN. The first path takes an empty string and returns the result generated from the PostList view, which is basically a list of posts for our homepage, and an optional parameter name for the view which will later be used in the templates

# Names are an optional parameter, but it is a good practice to give unique and rememberable names to views which makes our work easy while designing templates and it helps keep things organized as your number of URLs grows.

# Next, we have the generalized expression for the PostDetail views which resolve the slug (a string consisting of ASCII letters or numbers) Django uses angle brackets < > to capture the values from the URL and return the equivalent post detail page.

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

# Now we need to include these blog URLs to the actual project for doing so open the mysite/urls.py file.