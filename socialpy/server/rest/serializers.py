from rest_framework import serializers
from socialpy.server.data.models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name',)



class PostSerializer(serializers.HyperlinkedModelSerializer):
    categorys = CategorySerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ('pk', 'text', 'image', 'categorys')

    def set_categorys(self, post, categorys):
        post.categorys.clear()
        for c in categorys:
            category, created = Category.objects.get_or_create(**dict(c))
            post.categorys.add(category)
        return post

    def get_categorys(self, validated_data):
        if 'categorys' in validated_data:
            return validated_data.pop('categorys')
        return []

    def create(self, validated_data):
        categorys = self.get_categorys(validated_data)# validated_data.pop('categorys')
        print(categorys)
        post = Post.objects.create(**validated_data)
        return self.set_categorys(post, categorys)

    def update(self, instance, validated_data):
        #categorys = validated_data.pop('categorys')
        categorys = self.get_categorys(validated_data)
        post = super(PostSerializer, self).update(instance, validated_data)
        return self.set_categorys(post, categorys)


class CategorySerializerUrl(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rest:category-detail', read_only=True)

    class Meta:
        model = Category
        fields = ('url', 'pk', 'name',)

class PostSerializerUrl(PostSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rest:post-detail', read_only=True)
    categorys = CategorySerializerUrl(many=True, required=False)

    class Meta:
        model = Post
        fields = ('url', 'text', 'image', 'categorys')
