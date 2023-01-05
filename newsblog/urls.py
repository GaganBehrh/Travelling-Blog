from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('post_view/', views.PostView.as_view(), name='post_view'),
    path('add/', views.AddView.as_view(), name='add'),
    path('edit/<int:pk>', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
     
]