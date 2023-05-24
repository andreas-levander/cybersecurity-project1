from django.urls import path
from .views import homePage, registerPage, messagePageView, add, clear, loginPage, filter_messages



urlpatterns = [
    path('', homePage),
    path('messages/', messagePageView, name='messages_v1'),
    path('messages/add/', add),
    path('messages/clear/', clear),
    path('messages/filter/', filter_messages, name='filter'),
    path("auth/register/", registerPage, name='register'),
    path("auth/login/", loginPage, name='login')
]