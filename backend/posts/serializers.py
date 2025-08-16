from rest_framework import serializers
from .models import Post,Category,Tag

# Category 序列化器::支持递归嵌套
class RecursiveCategorySerializer(serializers.Serializer):
    # 用于递归地序列化父分类
    def to_representation(self, value):
        serializer = self.parent.__class__(value,context=self.context)
        return serializer.data
class CategorySerializer(serializers.ModelSerializer):
    parent = RecursiveCategorySerializer(read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','parent']

# Tag 序列化器
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

# Post 序列化器
class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many = True,read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'create_time',
            'last_change_time',
            'category',
            'tags',
        ]