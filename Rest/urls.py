"""
URL configuration for Rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("app1.urls")),
    path('api/', views.Studentlist.as_view()),
    path('api_add/', views.Studentlist_add.as_view()),
    path('api_dis/<int:pk>', views.Studentlist_display.as_view()),
    path('api_update/<int:pk>', views.Studentlist_add.as_view()),
    path('api_destroy/<int:pk>', views.Studentlist_destroy.as_view()),
]
