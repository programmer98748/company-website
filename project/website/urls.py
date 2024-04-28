from django.urls import path

from . import views 
app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/', views.project, name='project'),
    path('services/', views.services, name='services'),

]


