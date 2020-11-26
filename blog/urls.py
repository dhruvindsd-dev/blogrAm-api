from django.urls import include, path
from rest_framework.authtoken import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sign-up', signUp),
    path('get-token', getToken),
    path('get-user-blogs', getUserBlogs),
    path('new-user-blog', newUserBlog),
    path('get-all-blogs', getBlogs),
    path('get-blogs-from-tags', getBlogsFromTags),
    path('get-blog-from-id/<int:id>', getBlogFromId)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
