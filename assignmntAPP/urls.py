
from django.urls import path
from assignmntAPP import views

urlpatterns = [
    # first page
    path('',views.home_view,name="home"),

# second
    path('toures-travels',views.tures_travel_view,name="tures-travel"),

# third
    path('Assignment-paper',views.Assignment_Paper_view,name="Assignment-paper"),


    
]
