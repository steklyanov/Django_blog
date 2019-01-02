from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),  # as_view точка входа при вызове класса
    path('tags/', tags_list, name='tags_list_url'),  # в нем создается экземпляр класса и вызывается
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),  # соответствующий запросу метод
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail_url'),

]