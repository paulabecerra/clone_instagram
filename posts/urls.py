#Posts URLs#

#Django
from django.urls import path

#Views
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.ListPosts.as_view(),
        name='feed'
    ),
    path(
        route='posts/new/',
        view=views.CreatePost.as_view(),
        name='create_post'
    ),
]
