from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('job_add', views.job_add, name='job_add'),
    path('jobs', views.jobs, name='jobs'),
    

]