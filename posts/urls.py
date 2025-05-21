from django.urls import path
from .views import PostList
from .views_search import PostAPIView

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path("search/", PostAPIView.as_view({'get': 'list'}), name="post-search"),
]
