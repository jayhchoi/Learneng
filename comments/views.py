from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import Comment
from .forms import CommentForm

User = get_user_model()


def comment_create_view(request):
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        # Only members can write review
        if not request.user.is_member:
            messages.warning(request, "리뷰는 멤버만 작성할 수 있습니다.")
            return HttpResponseRedirect(next)

        leader_id = request.POST.get('leader_id')
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.member = request.user
            form.instance.leader = get_object_or_404(User, id=leader_id)
            form.save()
        else:
            print(form.errors)
            
        return HttpResponseRedirect(next)
    raise Http404