from django.urls import path

from . import views
urlpatterns = [
    path('', views.authlogin,name='login'),
    path('register/', views.authregister,name='register'),
    path('logout/', views.authlogout,name='logout'),
    
    
]