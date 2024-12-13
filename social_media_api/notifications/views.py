from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


@login_required
def mark_notification_as_read(request, notification_id):
    """
    Mark a specific notification as read.
    """
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    notification.read = True
    notification.save()

    return JsonResponse({'message': 'Notification marked as read.'})
