from django.urls import path

from .views import messagePageView, add, clear

urlpatterns = [
    path('', messagePageView, name='messages'),
    path('add/', add),
    path('clear/', clear)
]
