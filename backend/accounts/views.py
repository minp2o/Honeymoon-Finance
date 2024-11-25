
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomUserSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User

class CustomRegisterView(RegisterView):
    serializer_class = CustomUserSerializer
    
    
class UpdateSurveyView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user