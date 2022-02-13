from django.urls import path

from . import views

app_name = 'green'
urlpatterns = [
    path('', views.home, name='home'),
    path('group/', views.group, name='group'),
    path('group/<int:pk>', views.group_pk, name='group_pk'),
    path('<int:pk>/', views.plant, name='plant'),
    path('shelf/<int:pk>', views.shelf, name='shelf'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('log_out', views.log_out, name='log_out'),
    path('shelf/delete/<int:pk>', views.deletePlant, name='deletePlant'),
    path('test/', views.test, name='test'),

]