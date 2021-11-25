
from django.urls import path
from assignmntAPP import views

urlpatterns = [
#  start
    path('home/',views.home_view,name="home"),
# first
    path('',views.tures_travel_view,name="tures-travel"),
# second
    path('Assignment-paper',views.Assignment_Paper_view,name="Assignment-paper"),
# third
    path('Paper-Bags',views.Paper_Bags_view,name="Paper-Bag"),
    # four 
    path('Designer-Handbags',views.Designer_Handbags_view,name="Designer-Handbags"),
    # fivth 
    path('Writting-essay',views.Writting_an_Essay_view,name="Writting-essay"),
    # six
     path('Things-Remembered-Personalized-Gifts',views.Things_Remembered_Personalized_Gifts_view,name="Things-Remembered-Personalized"),

]
