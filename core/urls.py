from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('formation/', views.formation, name='formation'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('set-language/', views.set_language, name='set_language'),
    path('set-theme/', views.set_theme, name='set_theme'),
]
