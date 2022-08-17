# Create your view here.
import codecs
import csv

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from .models import Post
from .serializers import PostSerializer


# Viewset
class PostViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing blog post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination


    @action(detail=False, methods=["POST"])
    def upload_data(self, request):
        file = request.FILES.get("file")

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")

        data = list(reader)
        
        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)

        post_list = []
        for row in serializer.data:
            post_list.append(
                Post(
                    slug=row["slug"],
                    title=row["title"],
                    description=row["description"],
                    date=row["date"],
                    author_1=row["author_1"],
                    author_2=row["author_2"],
                    author_3=row["author_3"],
                    tags=row["tags"],
                    image=row["image"],
                    image_alt=row["image_alt"],
                )
            )
        Post.objects.bulk_create(post_list)

        return Response("Successfully uploaded the data")
