from django.urls import path
import app.views as view

urlpatterns = [
    path('predict/', view.index_render, name='say_hello'),
]