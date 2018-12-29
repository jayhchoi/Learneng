from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.generic import DeleteView

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
        leader_obj = get_object_or_404(User, id=leader_id)

        # Only one comment per leader is allowed
        if Comment.objects.filter(member=request.user, leader=leader_obj).exists():
            messages.warning(request, "이미 작성한 리뷰가 있습니다.")
            return HttpResponseRedirect(next)
        
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.member = request.user
            form.instance.leader = get_object_or_404(User, id=leader_id)
            form.save()
        else:
            print(form.errors)
            
        return HttpResponseRedirect(next)
    raise Http404


def comment_delete_view(request, pk):
    if request.method == 'POST':
        previous_page = request.POST.get('group_url', '/')
        comment = get_object_or_404(Comment, pk=pk, member=request.user)
        comment.delete()
        return redirect(previous_page)
    raise Http404
    

    