from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('',views.PostList.as_view(),name='all'),
    path('new/',views.CreatePost.as_view(),name='create'),
    path('by/(?P<username>[-\w]+)',views.UserPost.as_view(),name='for_user'),
    path('by/(?P<username>[-\w]+)/(?P<pk>\d+)/',views.PostDetail.as_view(),name='single'),
    path('delete/(?P<pk>\d+)/',views.DeletePost.as_view(),name='delete'),


]
