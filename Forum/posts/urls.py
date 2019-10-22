from django.urls import path
from . import views
from users import views as user_views
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView, 
	PostUpdateView,
	TagListView
	)

urlpatterns = [
    path('', PostListView.as_view(), name='posts-home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('posts/create/', PostCreateView.as_view(), name='posts-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='posts-update'),
    path('posts/<int:pk>/comment/', views.AddCommentToPost, name='posts-add-comment'),
    path('posts/tags', TagListView.as_view(), name='posts-view-tags')
]