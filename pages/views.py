from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView

from groups.models import Group


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        groups = Group.objects.order_by('-id')
        context['groups'] = groups
        context['members'] = get_user_model().objects.filter(is_student=True)
        context['leaders'] = get_user_model().objects.filter(is_teacher=True)
        return context
    

class AboutView(TemplateView):
    template_name = 'pages/about.html'