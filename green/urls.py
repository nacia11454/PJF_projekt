from django.urls import path

from . import views

app_name = 'green'
urlpatterns = [
    path('', views.home, name='home'),
    path('group/', views.GroupView.as_view(), name='group'),
    path('<int:pk>/', views.PlantView.as_view(), name='plant'),
    path('shelf/', views.shelf, name='shelf'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    path('test/', views.test, name='test'),

]