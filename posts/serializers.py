from rest_framework import serializers
from posts.models import Post
from tags.serializers import TagSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags_details = TagSerializer(source='tags', read_only=True, many=True)
    api_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created_on', 'author',
                  'tags_details', 'url', 'api_url', 'image', 'counter')
        read_only_fields = ('id', 'created_on', 'slug')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def get_api_url(self, obj):
        return "#/post/%s" % obj.slug
