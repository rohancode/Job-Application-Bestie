from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('jobs/add', views.job_add, name='job_add'),
    path('jobs/add/<job_id>', views.job_update, name='job_update'),
    path('jobs', views.jobs, name='jobs'),
    path('jobs/<job_id>', views.job_main, name='job_main'),
    
    

]