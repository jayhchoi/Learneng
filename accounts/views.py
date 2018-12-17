from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, FormView, View

from groups.models import Group
from .models import Profile
from .forms import SignupForm, CustomLoginForm, ProfileForm

User = get_user_model()


class LeaderGroupListView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/leader_group_list.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not request.user.is_leader:
            return redirect('pages:home')
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.filter(leader=self.request.user)
        return context


class MemberGroupListView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/member_group_list.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not request.user.is_member:
            return redirect('pages:home')
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.filter(members=self.request.user)
        return context


class SignupView(TemplateView):
    template_name = 'accounts/signup.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm


class LeaderSignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/leader_signup.html'

    def form_valid(self, form):
        user = form.save()  # creates a user instance by using the input of the form
        user.is_leader = True
        user.save()
        login(self.request, user)
        return redirect('pages:home')


class MemberSignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/member_signup.html'

    def form_valid(self, form):
        user = form.save()  # creates a user instance by using the input of the form
        user.is_member = True
        user.save()
        login(self.request, user)
        return redirect('pages:home')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(Profile, user=self.request.user)
        return context


# def profile_update_view(request):
#     profile = get_object_or_404(Profile, user=request.user)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:profile')
#     else:
#         form = ProfileForm(instance=profile)
#     context = {
#         'form': form
#     }
#     return render(request, 'accounts/profile_update.html', context)


class ProfileUpdateView(LoginRequiredMixin, View):
    form_class = ProfileForm
    template_name = 'accounts/profile_update.html'

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user)
        form = self.form_class(instance=profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user)
        form = self.form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        return render(request, self.template_name, {'form': form})


# Using signals to show messages
def show_logout_message(sender, user, request, **kwargs):
    messages.info(request, '로그아웃 되었습니다.')

user_logged_out.connect(show_logout_message)


def show_login_message(sender, user, request, **kwargs):
    messages.success(request, '{}님 환영합니다.'.format(user.name))

user_logged_in.connect(show_login_message)