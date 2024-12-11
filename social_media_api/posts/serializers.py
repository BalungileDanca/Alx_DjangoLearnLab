from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')  # To display the author's username
    post_title = serializers.ReadOnlyField(source='post.title')  # To display the post's title

    class Meta:
        model = Comment
        fields = ['id', 'post', 'post_title', 'author', 'author_username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']  # Fields auto-handled by the system


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')  # To display the author's username
    comments = CommentSerializer(many=True, read_only=True)  # Nested representation of comments

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['author', 'created_at', 'updated_at']  # Fields auto-handled by the system
