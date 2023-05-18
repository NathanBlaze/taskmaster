"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path

from tasks import views

urlpatterns = [
    path("", views.homepage),
    path("tareas/", views.list_tasks),
    path("tareas/alta", views.create_task),
    path("lab/", views.lab_view),
    path("temas/", views.list_subjects),
    path("temas/<int:pk>/", views.subject_detail),
    path("search/", views.search),
    path("admin/", admin.site.urls),
    # path("tareas/h/", views.list_high_priority),
    # path("tareas/n/", views.list_normal_priority),
    # path("tareas/l/", views.list_low_priority),
    re_path(r"^tareas/([nhl])/$", views.list_by_priority),
]
