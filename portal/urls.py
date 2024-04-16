from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerPage, name = "register"),  
    path('login', views.loginPage, name = "login"),  
    path('logout/', views.logoutUser, name = "logout"),  

    path('', views.homepage, name = "homepage"),
    path('datalogger', views.datalogger, name = "datalogger"),
    path('yourbuildings', views.yourBuildings, name = "yourbuildings"),
    path('buildingprofile/<str:pk>', views.buildingprofile, name = "buildingprofile"),

    path('updatebuilding/<str:pk>', views.updateBuilding, name = "updatebuilding"),

    path('buildingpdf/<str:pk>', views.buildingPDF, name = "buildingpdf"),
    path('pdf/<str:pk>', views.generatePDF, name = "pdf"),

    path('iot', views.iot, name = "iot"),
]