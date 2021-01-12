from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from notes import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.IndexView.as_view(), name='index'),
    path('<str:access_link>', views.IndexView.as_view(), name='index')
]
