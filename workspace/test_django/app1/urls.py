from django.urls import path

from . import views

app_name = 'app1'

urlpatterns = [
    path('list/', views.ListSchedule.as_view(), name='list'),
    path('create/', views.CreateSchedule.as_view(), name='create'),
    path('detail/<int:pk>', views.DetailSchedule.as_view(), name='detail'),
    path('update/<int:pk>', views.UpdateSchedule.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteSchedule.as_view(), name='delete'),
]
