from .models import Post
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)
from .documents import PostDocument
from .serializers import PostSearchSerializer



class PostAPIView(DocumentViewSet):
    document = PostDocument
    serializer_class = PostSearchSerializer
    
    fielddata = True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
    search_fields = ("title","body")
    multi_match_search_fields = (
        "title", "body"
    )

    filter_fields = {
        "title" : "title.raw",
        "body" : "body.raw",
    }

    ordering_fields = {
        "id": None,
        "title" : "title.raw",
        "date_created": "date_created",
        "last_updated": "last_updated",
    }
    ordering = ("-date_created", "-last_updated")
    
    