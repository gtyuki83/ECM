from django.shortcuts import render

# Create your views here.

# editのインポート
from django.views import generic
from . import models
from . import forms

from django.urls import reverse_lazy

# create作成


class CreateSchedule(generic.edit.CreateView):
    """
    #説明
    Create Schedule
    """

    template_name = 'app1/create_schedule.html'
    model = models.Schedules

    form_class = forms.CreateScheduleForm

    success_url = reverse_lazy('app1:list')


# list作成
class ListSchedule(generic.ListView):
    """
    List Schedule
    """

    template_name = 'app1/list_schedule.html'
    model = models.Schedules

    # querysetを追記
    queryset = model.objects.all


# updateも同じく作成
class UpdateSchedule(generic.edit.UpdateView):
    """
    Update Schedule
    """

    template_name = 'app1/update_schedule.html'
    model = models.Schedules

    form_class = forms.UpdateScheduleForm

    success_url = reverse_lazy('app1:list')


class DeleteSchedule(generic.DeleteView):
    """
    Delete Schedule
    """

    template_name = 'app1/delete_schedule.html'
    model = models.Schedules

    success_url = reverse_lazy('app1:list')


class DetailSchedule(generic.DetailView):
    """
    Detail Schedule
    """

    template_name = 'app1/detail_schedule.html'
    model = models.Schedules
