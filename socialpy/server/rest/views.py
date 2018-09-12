from rest_framework import viewsets
from socialpy.server.rest.serializers import CategorySerializer, PostSerializer, PostSerializerUrl
from socialpy.server.data.models import Category, Post

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all categorys in the db.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    The view set of the post model.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.request and self.request.accepted_renderer.format == 'api':
            return PostSerializerUrl
        return PostSerializer
