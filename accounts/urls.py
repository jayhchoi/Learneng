from django.urls import path
from django.contrib.auth import views as auth_views

from .views import LeaderGroupListView, MemberGroupListView, LeaderSignupView, MemberSignupView, SignupView

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signup/leader/', LeaderSignupView.as_view(), name='leader_signup'),
    path('signup/member', MemberSignupView.as_view(), name='member_signup'),
    path('my_group/leader/', LeaderGroupListView.as_view(), name='leader_group'),
    path('my_group/member/', MemberGroupListView.as_view(), name='member_group'),
]
