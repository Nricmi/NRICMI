from django.contrib import admin
from django.urls import path
from . import views
from .views import search_view, page_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('areas/', views.areas, name='areas'),
    path('facilities/', views.facilities, name='facilities'),
    path('opportunity/', views.opportunity, name='opportunity'),
    path('teams/', views.teams, name='teams'),
    path('gallery/', views.gallery, name='gallery'),
    path('mgu/', views.mgu, name='mgu'),
    path('form/', views.form, name='form'),
    path('dr/', views.dr, name='dr'),

    path('search/', search_view, name='search'),
    path('page/<int:pk>/', page_detail, name='page_detail'),

    path('submit/', views.submit, name='submit'),  

]
