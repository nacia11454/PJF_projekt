from django.urls import path

from . import views

app_name = 'green'
urlpatterns = [
    path('', views.home, name='home'),
    path('group/', views.GroupView.as_view(), name='group'),
    path('plant/', views.PlantsView.as_view(), name='plants'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:group_id>/like/', views.like, name='like'),
    path('login/',views.loginPage, name='login'),
    path('register/',views.registerPage, name='register'),
]