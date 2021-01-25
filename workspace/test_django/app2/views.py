from django.shortcuts import render

from django.urls import reverse_lazy

from django.views import generic
from . import models
# Create your views here.

from . import forms

# list作成


class ListUser(generic.ListView):
    """
    List User
    """

    template_name = 'app2/list_user.html'
    model = models.User

    queryset = model.objects.all


class CreateUser(generic.CreateView):
    """
    Create User
    """

    template_name = 'app2/create_user.html'
    model = models.User

    form_class = forms.CreateUserForm

    # 登録成功時の遷移するURLを指定します。
    success_url = reverse_lazy('app2:list')


class DetailUser(generic.DetailView):
    """
    Detail User
    """

    template_name = 'app2/detail_user.html'
    model = models.User


class UpdateUser(generic.UpdateView):
    """
    Update User
    """
    template_name = 'app2/update_user.html'
    model = models.User

    form_class = forms.UpdateUserForm

    success_url = reverse_lazy('app2:list')


class DeleteUser(generic.DeleteView):
    """
    Delete User
    """

    template_name = 'app2/delete_user.html'
    model = models.User

    form_class = forms.DeleteUserForm

    success_url = reverse_lazy('app2:list')
