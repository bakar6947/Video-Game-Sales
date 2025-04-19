from django.urls import path
import app.views as view

urlpatterns = [
    path('ml_app/', view.get_data, name="Get_User_Data"),
    path('predict/', view.make_prediction, name="Prediction")
]