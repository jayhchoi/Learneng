from django.urls import path

from .views import TeacherProfileView, StudentProfileView

app_name = 'accounts'
urlpatterns = [
    path('profile/teacher/', TeacherProfileView.as_view(), name='teacher_profile'),
    path('profile/student/', StudentProfileView.as_view(), name='student_profile'),
]
