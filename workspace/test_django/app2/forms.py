from django.forms import ModelForm
# modelsファイル（モジュール）をimport
from . import models

# create_schedule.htmlのためのフォームを作成


class CreateUserForm(ModelForm):
    """
    for CreateSchedule
    """

    # classの中にclassを作るという謎ですが、ModelFormの使い方はもう決まっています！
    class Meta:

        # データを入れたいモデル名を指定
        model = models.User

        # モデルの中でデータを入れたい項目をリストやタプルで指定します。すべての場合は '__all__'でもOKです。
        fields = '__all__'


class UpdateUserForm(ModelForm):
    """
    for UpdateSchedule
    """

    class Meta:
        model = models.User
        fields = '__all__'


class DeleteUserForm(ModelForm):
    """
    for DeleteSchedule
    """

    class Meta:
        model = models.User
        fields = '__all__'
