from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

        
def get_data(request):
    
    if request.method == 'POST':
        
        Name = request.POST.get('game_name')
        platform = request.POST.get('Platform')
        genre = request.POST.get('Genre')
        publisher = request.POST.get('Publisher')
        na_sale = request.POST.get('NA_Sales')
        eu_sale = request.POST.get('EU_Sales')
        jp_sale = request.POST.get('JP_Sales')
        other_sale = request.POST.get('Other_Sales')
        year = request.POST.get('Year')
        
        custom_obj = CustomData(
            platform = platform,
            gener = genre,
            publisher = publisher,
            NA_sales = na_sale,
            EU_sales = eu_sale,
            JP_sales = jp_sale,
            other_sales = other_sale,
            year = year 
        )
        
        data_point = custom_obj.get_data_transfor_as_df()
        predict_pipe = PredictPipeline()
        prediction = predict_pipe.predict(data_point)
        
        context = {
            'name': Name,
            'prediction': round(float(prediction), 2)
        }
        return render(request, 'predict.html', context)
        
    return render(request, 'form.html')




def make_prediction(request):
    return render(request, 'predict.html')