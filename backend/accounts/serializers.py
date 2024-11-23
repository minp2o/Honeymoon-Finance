from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=30, required=False, allow_blank=True)
    gender = serializers.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], required=False, allow_blank=True)
    age = serializers.IntegerField(required=True)
    phone = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'nickname': self.validated_data.get('nickname', ''),
            'gender': self.validated_data.get('gender', ''),
            'age': self.validated_data.get('age', ''),
            'phone': self.validated_data.get('phone', ''),
        })
        return data

    def save(self, request):
        user = super().save(request)
        user.nickname = self.cleaned_data.get('nickname')
        user.gender = self.cleaned_data.get('gender')
        user.age = self.cleaned_data.get('age')
        user.phone = self.cleaned_data.get('phone')
        user.save()
        return user

class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'nickname', 'gender', 'age', 'phone')
        read_only_fields = ('id', 'username', 'email')