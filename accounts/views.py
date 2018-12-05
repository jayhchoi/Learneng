from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from groups.models import Group
from .forms import SignupForm

User = get_user_model()

class TeacherProfileView(TemplateView):
    template_name = 'accounts/profile_teacher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.filter(leader=self.request.user)
        return context


class StudentProfileView(TemplateView):
    template_name = 'accounts/profile_student.html'

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
        messages.info(self.request, "Thank you for signing up. Have fun teaching English!")        
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
        messages.info(self.request, "Thank you for signing up. Have fun learning English!")        
        return redirect('pages:home')