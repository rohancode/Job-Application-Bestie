from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('jobs/add', views.job_add, name='job_add'),
    path('jobs/<job_id>/edit', views.job_update, name='job_update'),
    path('jobs', views.jobs, name='jobs'),
    path('jobs/<job_id>/delete', views.job_delete, name='job_delete'),

    path('cl/<job_id>', views.cl_main, name='cl_main'),
    path('cl/<cl_id>/proofread', views.cl_proofread, name='cl_proofread'),
    path('cl/<cl_id>/download', views.cl_download, name='cl_download'),

    path('source/add', views.source_add, name='source_add'),
    path('source/<source_id>/edit', views.source_update, name='source_update'),
    path('source/<source_id>/delete', views.source_delete, name='source_delete'),

    path('references', views.references_main, name='references_main'),
    path('project/add', views.project_add, name='project_add'),
    path('project/<project_id>/edit', views.project_update, name='project_update'),
    path('project/<project_id>/delete', views.project_delete, name='project_delete'),
    path('project/<project_id>', views.project_main, name='project_main'),

    path('accept_cookies', views.accept_cookies, name='accept_cookies'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('terms_conditions', views.terms_conditions, name='terms_conditions'),
    path('data_security', views.data_security, name='data_security'),
    
    path('ui_dev_index_footer', views.ui_dev_index_footer, name='ui_dev_index_footer'),
    

]