from django.urls import path
from .views import event_list, event_detail

urlpatterns = [
    path('', event_list, name='event_list'),  # This should match 'events/'
    path('<int:event_id>/', event_detail, name='event_detail'),  # For event details
]
