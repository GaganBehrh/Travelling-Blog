from . import views
from django.urls import path, re_path


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('post_view/', views.PostView.as_view(), name='post_view'),
    path('add/', views.AddView.as_view(), name='add'),
    path('tripcalculator/', views.TripCalculatorView.as_view(), name='tripcalculator'),
    path('edit/<int:pk>', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
    path('contact/<int:pk>', views.contact_views.as_view(), name='contact'),  
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
   
]
   
     
