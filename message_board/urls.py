from django.urls import path

from .views import messagePageView, add

urlpatterns = [
    path('', messagePageView, name='messages'),
    path('add/', add)
]
