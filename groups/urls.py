from django.urls import path

from .views import (
    GroupListView,
    GroupDetailView,
    GroupCreateView,
    GroupUpdateView,
    GroupDeleteView,
    group_join_view,
    group_leave_view,
    # email_view
)

app_name = 'groups'
urlpatterns = [
    path('', GroupListView.as_view(), name='list'),
    path('<int:pk>/', GroupDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', GroupUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='delete'),
    path('<int:pk>/join/', group_join_view, name='join'),
    path('<int:pk>/leave/', group_leave_view, name='leave'),
    path('create/', GroupCreateView.as_view(), name='create'),
    # path('email/', email_view, name='email'),
]