from django.urls import path

from blog.views import PostView

urlpatterns = [
    path('post/<slug:slug>/', PostView.as_view(), name="post")
]
