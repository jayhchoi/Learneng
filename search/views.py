from django.shortcuts import render
from django.views.generic import ListView

from groups.models import Group


class SearchGroupView(ListView):
    model = Group
    template_name = 'groups/group_list.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id')

        # Group name
        if 'group' in self.request.GET:
            group = self.request.GET.get('group')
            if group:
                queryset = queryset.filter(
                    name__icontains=group)

        # Level
        if 'level' in self.request.GET:
            level = self.request.GET.get('level')
            if level:
                queryset = queryset.filter(
                    level__iexact=level)

        # Start date
        if 'start_date' in self.request.GET:
            start_date = self.request.GET.get('start_date')
            if start_date:
                queryset = queryset.filter(
                    start_date__gte=start_date)

        # teacher
        if 'teacher' in self.request.GET:
            teacher = self.request.GET.get('teacher')
            if teacher:
                queryset = queryset.filter(
                    leader__name__icontains=teacher)

        # Location
        if 'location' in self.request.GET:
            location = self.request.GET.get('location')
            if location:
                queryset = queryset.filter(
                    location__icontains=location)

        # Day
        if 'day' in self.request.GET:
            day = self.request.GET.get('day')
            if day:
                queryset = queryset.filter(
                    day__icontains=day)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queries'] = [
            self.request.GET.get('group'),
            self.request.GET.get('level'),
            self.request.GET.get('date'),
            self.request.GET.get('teacher'),
            self.request.GET.get('location')
        ]
        return context
        