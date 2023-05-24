from django.urls import path
from .views import homePage, registerPage, messagePageView, add, clear, loginPage



urlpatterns = [
    path('', homePage),
    path('messages/', messagePageView, name='messages_v1'),
    path('messages/add/', add),
    path('messages/clear/', clear),
    path("auth/register/", registerPage, name='register'),
    path("auth/login/", loginPage, name='login')
]