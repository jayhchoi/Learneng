from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .forms import GroupForm
from .models import Group
from comments.models import Comment
from comments.forms import CommentForm


class GroupListView(ListView):
    model = Group
    template_name = 'groups/group_list.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id') #.filter(start_date__gte=datetime.now()) Change this before production
        return queryset


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups/group_detail.html'

    def get_context_data(self, **kwargs):
        obj = self.get_object()
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(leader=obj.leader).order_by('-pk')
        context['form'] = CommentForm()
        return context
    

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'groups/group_create.html'
    form_class = GroupForm

    def get(self, request, *args, **kwargs):
        self.object = None
        # Check if the user is teacher
        if request.user.is_leader == False:
            messages.warning(request, "스터디 개설은 리더만 가능합니다.")
            return redirect('pages:home')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        group = form.save(commit=False)  # creates a group instance by using the input of the form
        group.leader = self.request.user
        group.save()
        messages.success(self.request, "새 그룹 생성이 완료되었습니다.")        
        return redirect(group.get_absolute_url())


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'groups/group_update.html'
    form_class = GroupForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Check if current user is the owner of this instance
        if self.object.leader != request.user:
            messages.warning(request, "해당 스터디에 대한 권한이 없습니다.")
            return redirect('pages:home')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "기존 그룹이 업데이트 되었습니다.")
        return redirect('groups:detail', pk=self.object.id)


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups/group_delete.html'
    success_url = reverse_lazy('groups:list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.leader != request.user:
            messages.warning(request, "해당 스터디에 대한 권한이 없습니다.")
            return redirect('pages:home')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


@login_required
def group_join_view(request, **kwargs):
    pk_ = kwargs['pk'] # This is from the url, or request.path
    group = get_object_or_404(Group, pk=pk_)
    user = get_user(request)

    if user in group.members.all():
        messages.warning(request, '이미 해당 그룹의 멤버입니다.')
        return redirect(group.get_absolute_url())

    if group.members.count() >= group.size:
        messages.warning(request, '해당 그룹은 정원이 초과되었습니다.')
        return redirect('pages:home')

    if request.method == "POST":
        contact_ = request.POST.get('contact')
        group.members.add(user)
        # group.save() m2m field는 따로 save() 필요없음 그래서, signal 쓸때 m2m_changed 써야함
        user.contact = contact_
        user.save()
        messages.success(request, "그룹 참여가 완료되었습니다.")
        return redirect(group.get_absolute_url())
    
    context = {
        'group': group
    }
    return render(request, 'groups/group_join.html', context)


@login_required
def group_leave_view(request, **kwargs):
    pk_ = kwargs['pk']
    group = get_object_or_404(Group, pk=pk_)
    user = get_user(request)

    if user not in group.members.all():
        messages.warning(request, "해당 그룹의 멤버가 아닙니다.")
        return redirect(group.get_absolute_url())

    if request.method == "POST":
        group.members.remove(user)
        messages.success(request, '그룹 탈퇴가 완료되었습니다.')
        return redirect('groups:list')
    
    context = {
        'group': group
    }
    return render(request, 'groups/group_leave.html', context)


# def email_view(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['jaychoi1619@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('pages:home')
#     return render(request, "groups/email_form.html", {'form': form})