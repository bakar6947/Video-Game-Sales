from django.shortcuts import render, HttpResponse
# Create your views here.




def index_render(request):
    return render(request, 'index.html')