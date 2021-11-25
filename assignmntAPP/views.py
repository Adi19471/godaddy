from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request,"ASS/home.html")

def tures_travel_view(request):
    return render(request,"ASS/1tures_travel.html")


def Assignment_Paper_view(request):
    return render(request,"ASS/2Assignment_Paper.html")


def Paper_Bags_view(request):
    return render(request,"ASS/3Paper_Bags.html")

# fourth dada kalandar 
def Designer_Handbags_view(request):
    return render(request,"ASS/4Designer_Handbags.html")
# fivth 

def Writting_an_Essay_view(request):
    return render(request,"ASS/5Writting_an_Essay_.html")

def Things_Remembered_Personalized_Gifts_view(request):
    return render(request,"ASS/6Things_Remembered_Personalized_Gifts_view.html")
