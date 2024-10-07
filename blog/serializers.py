from django.contrib.auth.models import User
from .models import BlogPost, Category, Tag
from rest_framework import serializers

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Tag serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

# BlogPost serializer# BlogPost serializer
class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)   
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all()) 

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'published_date', 'created_date']

    def validate_category(self, value):
        if not Category.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Invalid category.")
        return value

    def validate_tags(self, value):
        if not all(Tag.objects.filter(id=tag.id).exists() for tag in value):
            raise serializers.ValidationError("One or more tags are invalid.")
        return value