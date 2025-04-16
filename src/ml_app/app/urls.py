from django.urls import path
from app.views import say_hello

urlpatterns = [
    path('predict/', say_hello, name='say_hello'),
]