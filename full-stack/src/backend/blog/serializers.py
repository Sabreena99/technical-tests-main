from itertools import product
from rest_framework import serializers

from .models import Post


# Serializer
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"