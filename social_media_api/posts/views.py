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
from django.contrib.contenttypes.models import ContentType

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    # Check if the user has already liked the post
    if Like.objects.filter(post=post, user=user).exists():
        return JsonResponse({'error': 'You have already liked this post.'}, status=400)

    # Create a like
    Like.objects.create(post=post, user=user)

    # Create a notification
    Notification.objects.create(
        recipient=post.author,  # Assuming Post has an author field
        actor=user,
        verb='liked',
        target=post,
    )

    return JsonResponse({'message': 'Post liked successfully.'})


@login_required
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    # Check if the user has liked the post
    like = Like.objects.filter(post=post, user=user).first()
    if not like:
        return JsonResponse({'error': 'You have not liked this post.'}, status=400)

    # Delete the like
    like.delete()

    return JsonResponse({'message': 'Post unliked successfully.'})

@login_required
def fetch_notifications(request):
    """
    Fetch all notifications for the authenticated user, 
    showing unread notifications prominently.
    """
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    unread_notifications = notifications.filter(read=False)

    data = {
        'unread': [
            {
                'id': notif.id,
                'actor': notif.actor.username,
                'verb': notif.verb,
                'target': str(notif.target),
                'timestamp': notif.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            }
            for notif in unread_notifications
        ],
        'all': [
            {
                'id': notif.id,
                'actor': notif.actor.username,
                'verb': notif.verb,
                'target': str(notif.target),
                'timestamp': notif.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'read': notif.read,
            }
            for notif in notifications
        ],
    }

    return JsonResponse(data)


