from django.urls import path
from . import views

app_name="loan"
urlpatterns = [
    path('', views.index, name="loan"),
    
]