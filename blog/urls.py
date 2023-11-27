from django.urls import path

from blog.views import PostView, TagView

urlpatterns = [
    path('post/<slug:slug>/', PostView.as_view(), name="post"),
    path('tag/<str:name>/', TagView.as_view(), name="tag"),
]
