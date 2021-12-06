from django.urls import path
from . import views


urlpatterns = [
    path('', views.ForumListView.as_view(), name='forum'),
    path('newPost/', views.ThreadCreateView.as_view(), name='new_thread'),
    path('comment/create/<int:thread_id>/', views.CommentCreateView.as_view(), name='new_comment'),
    path('newPost/<int:pk>', views.ThreadDetailView.as_view(), name='view_post'),
    path('<int:pk>/deleteThread/', views.DeleteThread.as_view(), name='delete_thread'),

]

