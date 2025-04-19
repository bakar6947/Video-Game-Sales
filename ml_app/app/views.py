from django.shortcuts import render, HttpResponse
# Create your views here.

from src.pipeline.predict_pipeline import CustomData, PredictPipeline



def get_data(request):
    
    if request.method == 'POST':
        pass
    
    return render(request, 'form.html')




def make_prediction(request):
    
    return render(request, 'predict.html')