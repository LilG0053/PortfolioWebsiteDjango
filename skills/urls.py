from django.urls import path
from . import views

urlpatterns = [
    path('', views.skill_list, name='skill_list'),
    path('skills/<int:skill_id>/projects/', views.skill_detail_redirect, name='skill_detail_redirect'),
]