from django.urls import path

from .views import (
    SearchGroupView,
)

app_name = 'search'
urlpatterns = [
    path('', SearchGroupView.as_view(), name='query'),
]