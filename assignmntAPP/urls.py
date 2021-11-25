
from django.urls import path
from assignmntAPP import views

urlpatterns = [
    path('',views.home_view,name="home")
    
]
