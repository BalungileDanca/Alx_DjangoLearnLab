from django.urls import path
from . import views

urlpatterns = [
    path('fetch/', views.fetch_notifications, name='fetch_notifications'),
    path('mark-as-read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
]