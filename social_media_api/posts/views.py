from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import viewsets
from .models import Post, Comment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly



class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author']  # Filter by exact matches (e.g., author ID)
    search_fields = ['title', 'content']  # Search by title or content

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Fetch the users the current user is following
        following_users = request.user.following.all()

        # Fetch posts authored by these users, ordered by creation time
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from notifications.models import Notification
from rest_framework import generics
from django.contrib.contenttypes.models import ContentType

@login_required
def like_post(request, pk):
    """
    Allows an authenticated user to like a post.
    If the user already liked the post, no duplicate is created.
    """
    # Safely retrieve the post or return a 404 error
    post = generics.get_object_or_404(Post, pk=pk)

    # Get or create a like for this post and user
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        # Create a notification if the like was just created
        Notification.objects.create(
            recipient=post.author,  # Assuming Post has an 'author' field
            actor=request.user,
            verb='liked',
            target=post,
        )
        return JsonResponse({'message': 'Post liked successfully.'})
    else:
        return JsonResponse({'message': 'You already liked this post.'}, status=400)


@login_required
def unlike_post(request, pk):
    """
    Allows an authenticated user to unlike a post if they have already liked it.
    """
    # Safely retrieve the post or return a 404 error
    post = generics.get_object_or_404(Post, pk=pk)

    # Check if the like exists
    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        # Delete the like
        like.delete()
        return JsonResponse({'message': 'Post unliked successfully.'})
    else:
        return JsonResponse({'message': 'You have not liked this post.'}, status=400)