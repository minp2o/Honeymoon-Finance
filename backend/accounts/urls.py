# accounts/urls.py

from django.urls import path
from .views import CustomRegisterView,UpdateSurveyView

urlpatterns = [
    path('register/', CustomRegisterView.as_view(), name='custom_register'),
    path('survey/', UpdateSurveyView.as_view(), name='update_survey'),
    
]