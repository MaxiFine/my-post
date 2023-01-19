from django.urls import path
from . import views


urlpatterns = [
    
    # viewing urls
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('drafts/', views.post_draft_list, name='draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),

    # Editng urls
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete/<int:pk>/', views.post_remove, name='post_delete'),
    
    
    # for commenting
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('comment/<int:pk>/delete-comment/', views.comment_delete, name='delete_comment'),
    path('comment/<int:pk>/edit-comment/', views.edit_comment, name='comment_edit'),

]

