from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from groups.models import Group
from .forms import SignupForm

User = get_user_model()


class TeacherProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile_teacher.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not request.user.is_teacher:
            return redirect('pages:home')
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.filter(leader=self.request.user)
        return context


class StudentProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile_student.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not request.user.is_student:
            return redirect('pages:home')
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.filter(members=self.request.user)
        return context


class SignupView(TemplateView):
    template_name = 'accounts/signup.html'


class TeacherSignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup_teacher.html'

    def form_valid(self, form):
        user = form.save()  # creates a user instance by using the input of the form
        user.is_teacher = True
        user.save()
        login(self.request, user)
        return redirect('pages:home')


class StudentSignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup_student.html'

    def form_valid(self, form):
        user = form.save()  # creates a user instance by using the input of the form
        user.is_student = True
        user.save()
        login(self.request, user)
        return redirect('pages:home')


# Using signals to show messages
def show_logout_message(sender, user, request, **kwargs):
    messages.info(request, '로그아웃 되었습니다.')

user_logged_out.connect(show_logout_message)


def show_login_message(sender, user, request, **kwargs):
    messages.success(request, '{}님 환영합니다.'.format(user.name))

user_logged_in.connect(show_login_message)