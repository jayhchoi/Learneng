from django.urls import path

from .views import comment_create_view, comment_delete_view


app_name = 'comments'
urlpatterns = [
    path('create/', comment_create_view, name='create'),
    path('<int:pk>/delete/', comment_delete_view, name='delete'),
]