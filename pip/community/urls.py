from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('bellschedule/', views.bellschedule, name='bellschedule'),
    path('mealmenu/', views.mealmenu, name='mealmenu'),
    path('post/new', views.post_new, name='post_new'),
     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
     path('about/',views.about,name='about'),
     url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

]