from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

from .models import Comment
from .forms import CommentForm

User = get_user_model()


def comment_create_view(request):
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        leader_id = request.POST.get('leader_id')
        print(leader_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.member = request.user
            form.instance.leader = get_object_or_404(User, id=leader_id)
            form.save()
        return HttpResponseRedirect(next)