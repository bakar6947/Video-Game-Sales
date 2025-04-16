from django.shortcuts import render, HttpResponse
# Create your views here.

from src.pipeline.predict_pipeline import CustomData, PredictPipeline




def index_render(request): 
    if request.method == 'POST':
       pass
   
    return render(request, 'index.html')