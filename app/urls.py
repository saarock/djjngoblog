from django.urls import path, include, re_path
from .views import Home, add_blogs, blogs, blog, handel_comments, blog_popular
urlpatterns = [
    path('', Home, name="Home"),
    path('addBlogs/', add_blogs, name="UploadBlogs"),
    path('blogs/', blogs, name="Blogs"),
    path('blogs/<int:params>/', blog, name="Single blog"),
    path('blogs/0/<int:params>/', blog, name="Popular blog"),
    path('blogs/1/<int:params>/', blog_popular, name="Popular blog"),
    path("blogs/<int:params>/comment", handel_comments, name="Add_comment")
]
