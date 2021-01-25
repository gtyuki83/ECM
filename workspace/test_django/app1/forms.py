#coding: utf-8

from django.forms import ModelForm

from . import models


class CreateScheduleForm(ModelForm):
    """
    for CreateSchedule
    """

    class Meta:
        model = models.Schedules

        fields = '__all__'


class UpdateScheduleForm(ModelForm):
    """
    for UpdateSchedule
    """

    class Meta:
        model = models.Schedules

        fields = '__all__'


class DeleteScheduleForm(ModelForm):
    """
    For DeleteSchedule
    """

    class Meta:
        mdoel = models.Schedules

        fields = '__all__'
