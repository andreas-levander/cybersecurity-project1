from django.urls import path
from django.contrib.auth import views as auth_views
from .views import messagePageView, add, clear

urlpatterns = [
    path('messages/', messagePageView, name='messages'),
    path('messages/add/', add),
    path('messages/clear/', clear),
    path("auth/login/", auth_views.LoginView.as_view(), name='login'),
]
