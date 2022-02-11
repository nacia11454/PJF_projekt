from django.urls import path

from . import views

app_name = 'green'
urlpatterns = [
    path('', views.home, name='home'),
    path('group/', views.GroupView.as_view(), name='group'),
    path('plant/', views.plant, name='plant'),
    path('<int:pk>/', views.PlantView.as_view(), name='plante'),
    path('shelf/', views.shelf, name='shelf'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    path('test/', views.TestView.as_view(), name='test'),

]