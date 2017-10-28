from rest_framework import permissions
from posts.models import Post
from posts.serializers import PostSerializer
from posts.permissions import IsOwnerOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import generics

class PostFilter(filters.FilterSet):

    class Meta:
        model = Post
        fields = ['tags__name']

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(is_active=True).order_by('-updated_on')
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_class = PostFilter
    search_fields = ("title","description","tags__name")

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a board instance.
    """
    queryset = Post.objects.filter(is_active=True).order_by('-updated_on')
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_field = 'slug'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        obj.counter +=1
        obj.save()
        return obj
