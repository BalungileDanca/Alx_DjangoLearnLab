from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


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


@login_required
def mark_notification_as_read(request, notification_id):
    """
    Mark a specific notification as read.
    """
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    notification.read = True
    notification.save()

    return JsonResponse({'message': 'Notification marked as read.'})