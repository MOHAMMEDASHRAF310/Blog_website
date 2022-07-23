from django.urls import path
from .views import BlogListView ,BlogDetialView , BlogCreateView, BlogUpdateView ,BlogDeleteView
urlpatterns = [
    path('post/<int:pk>/',BlogDetialView.as_view(),name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('post/new',BlogCreateView.as_view(),name='post-new'),
    path('post/<int:pk>/update',BlogUpdateView.as_view(),name='post-edit'),
    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='post-delete'),
]