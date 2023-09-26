from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('jobs/add', views.job_add, name='job_add'),
    path('jobs/<job_id>/edit', views.job_update, name='job_update'),
    path('jobs', views.jobs, name='jobs'),
    path('jobs/<job_id>', views.job_main, name='job_main'),
    path('jobs/<job_id>/delete', views.job_delete, name='job_delete'),

    path('cl/<job_id>/add', views.cl_add, name='cl_add'),
    path('cl/<cl_id>/edit', views.cl_update, name='cl_update'),
    path('cl/<cl_id>/delete', views.cl_delete, name='cl_delete'),
    path('cl/<cl_id>/download', views.cl_download, name='cl_download'),
    
    
    

]