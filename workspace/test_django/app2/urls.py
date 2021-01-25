from django.urls import path

from . import views

app_name = 'app2'

urlpatterns = [
    path('list/', views.ListUser.as_view(), name='list'),
    path('create/', views.CreateUser.as_view(), name='create'),
    path('detail/<int:pk>', views.DetailUser.as_view(), name='detail'),
    path('update/<int:pk>', views.UpdateUser.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteUser.as_view(), name='delete'),
]
