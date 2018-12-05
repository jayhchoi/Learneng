from django.urls import path
from django.contrib.auth import views as auth_views

from .views import HomeView, AboutView
from accounts.views import SignupView, TeacherSignupView, StudentSignupView

app_name = 'pages'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signup/teacher/', TeacherSignupView.as_view(), name='teacher_signup'),
    path('signup/student', StudentSignupView.as_view(), name='student_signup'),
]
