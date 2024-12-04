from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.home),
    path('home2',views.home1),
    path('home3',views.home2),
    path('home4/<int:id>/', views.home3),
    path('home5/<int:id>/', views.home4),

]