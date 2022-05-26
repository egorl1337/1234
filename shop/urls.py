from django import views
from . import views
from django.contrib import admin
from django.urls import path, include, re_path
from shop.views import comments_edit, New_detail_view
from django.urls import re_path as url
from .views import Items


urlpatterns = [
    path('', views.index_shop, name = 'index_shop'),
    path('/comments/', views.comments, name = 'comments'),
    path('<int:pk>', views.New_detail_view, name = 'detail_view'),
    #url(r'^(?P<slug>[-\w]+)/$', views.New_detail_view, name = 'detail_view'),
    path('/comments/edit<int:pk>', views.comments_edit.as_view(), name = 'comments_edit'),   
    path('/comments/delete<int:pk>', views.comments_delete.as_view(), name = 'comments_delete')
]


