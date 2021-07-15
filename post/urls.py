from django.urls import path
from .views import post_view, home_view,post_detail_view,delete_post_view,add_comment_view

urlpatterns = [
    path('Add_post/',post_view, name='Add Post'),
    path('home/', home_view, name='home'),
    path('post_detail/<int:id>', post_detail_view, name='detail_post'),
    path('post_detail/<int:id>/post_delete', delete_post_view, name='post_delete'),
    path('post_detail/<int:id>/add_comment',add_comment_view, name='add_comment'),
]