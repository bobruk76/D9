from app.views import PostList, PostDetail
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),

    path('categories/', PostList.as_view(), name='category-list'),
    path('categories/<int:pk>', PostDetail.as_view(), name='category-detail'),
]