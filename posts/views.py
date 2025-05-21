from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .tasks import add

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        print("Getting queryset")
        post_id = Post.objects.all().first().id
        add.delay(post_id)
        return Post.objects.all()