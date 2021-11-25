from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request,"ASS/index.html")

def tures_travel_view(request):
    return render(request,"ASS/tures_travel.html")


def Assignment_Paper_view(request):
    return render(request,"ASS/Assignment_Paper.html")