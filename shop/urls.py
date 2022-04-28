from django import views
from . import views
from django.contrib import admin
from django.urls import path, include
from shop.views import comments_edit


urlpatterns = [
    path('', views.index_shop, name = 'index_shop'),
    path('/comments/', views.comments, name = 'comments'),
    path('<int:pk>', views.New_detail_view.as_view(), name = 'detail_view'),
    path('/comments/edit<int:pk>', views.comments_edit.as_view(), name = 'comments_edit'),   
    path('/comments/delete<int:pk>', views.comments_delete.as_view(), name = 'comments_delete')
]


