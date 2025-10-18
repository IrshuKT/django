"""
URL configuration for second_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<pk>', views.edit, name='edit'),
    path('delet/<pk>', views.delete, name='delete'),
    path('list/', views.list, name='list'),
    path('director/', views.director, name='director'),
    path('director_list/', views.director_list, name='director_list'),
    path('censor_info/', views.censor_info, name='censor_info'),
    path('actor/', views.actor, name='actor'),
    path('actor_list/', views.actor_list, name='actor_list'),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)