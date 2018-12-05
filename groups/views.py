from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib import messages

from .models import Group
from .forms import GroupForm

# HELPER FUNCTIONS
# def get_selected_group(request):
#     '''
#     This function works only when there is
#     'group_id' in the request.session
#     '''
#     group_id = request.POST.get('group_id')
#     selected_group = request.session['group_name'] # This is mere text!
#     selected_group = Group.objects.filter(
#         membership_type=membership_type
#     )
#     if selected_membership_qs.exists():
#         return selected_membership_qs.first()
#     return None



# VIEWS

class GroupListView(ListView):
    model = Group
    template_name = 'groups/group_list.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id') #.filter(start_date__gte=datetime.now())
        return queryset


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups/group_detail.html'

    def post(self, request, **kwargs):
        group_id = request.POST.get('group_id') # <-- this is a name attribute in forms from html template
        selected_group = Group.objects.get(id=group_id)
        current_user = request.user

        if current_user not in selected_group.members.all():
            selected_group.members.add(current_user)
            messages.info(request, "You've now successfully joined the group!")
            return redirect(reverse('groups:list'))
        else:
            messages.info(request, "You are already in the group!")
            return redirect(request.META.get("HTTP_REFERER"))
    

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'groups/group_create.html'
    form_class = GroupForm

    def form_valid(self, form):
        group = form.save(commit=False)  # creates a group instance by using the input of the form
        group.leader = self.request.user
        group.save()
        messages.info(self.request, "Your group is created successfully")        
        return redirect('groups:list')


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'groups/group_update.html'
    form_class = GroupForm

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Your group is updated successfully")        
        return redirect('groups:list')


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups/group_delete.html'
    success_url = reverse_lazy('groups:list')


@login_required
def group_join_view(request, **kwargs):
    pk_ = kwargs['pk']
    if request.method == "POST":
        group = get_object_or_404(Group, pk=pk_)
        if request.user in group.members.all():
            messages.info(request, 'You are already in the group!')
            return redirect(reverse('groups:detail', kwargs={'pk':pk_}))
        else:
            group.members.add(request.user)
            group.save()
            messages.info(request, "You are now in the group!")
            return redirect(reverse('groups:detail', kwargs={'pk':pk_}))
    return render(request, 'groups/group_join.html', {})


@login_required
def group_leave_view(request, **kwargs):
    pk_ = kwargs['pk']
    if request.method == "POST":
        group = get_object_or_404(Group, pk=pk_)
        if request.user in group.members.all():
            group.members.remove(request.user)
            messages.info(request, 'You\'ve just left the group!')
            return redirect(reverse('groups:list'))
        else:
            messages.info(request, "You are not in the group. Join first!")
            return redirect(reverse('groups:detail', kwargs={'pk':pk_}))
    return render(request, 'groups/group_leave.html', {})