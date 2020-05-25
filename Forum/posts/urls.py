from django.urls import path
from . import views
from users import views as user_views
from .views import (
	#PostDetailView, 
	PostCreateView, 
	PostUpdateView,
	PostUpvote,
	)

urlpatterns = [
    path('', views.home, name='posts-home'),

    path('posts/<int:pk>/', views.PostDetailView, name='posts-detail'),
    path('posts/create/', PostCreateView.as_view(), name='posts-create'),

    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='posts-update'),
    path('posts/<int:pk>/comment/', views.AddCommentToPost, name='posts-add-comment'),

    path('posts/tags/<slug:tag>/', views.tagFilter, name='posts-view-tags'),

    path('settings/', views.settings, name='posts-settings'),
    path('vote/<int:pk>',PostUpvote.as_view() , name="upvote"),

    path('posts/search', views.search, name='posts-search'),
    path('posts/subscribetag', views.TagSubscribe, name='tag-subscribe')
]