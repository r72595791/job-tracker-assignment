from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add/', views.job_create, name='job_create'),
    path('<int:id>/', views.job_detail, name='job_detail'),
    path('<int:id>/edit/', views.job_update, name='job_update'),
    path('<int:id>/delete/', views.job_delete, name='job_delete'),
]
