from django.urls import path

from .views import comment_create_view


app_name = 'comments'
urlpatterns = [
    path('create/', comment_create_view, name='create'),
]