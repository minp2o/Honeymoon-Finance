from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=30, required=False, allow_blank=True)
    gender = serializers.ChoiceField(choices=[('M', '남성'), ('F', '여성')], required=False, allow_blank=True)
    age = serializers.IntegerField(required=True)
    phone = serializers.CharField(required=True)
    has_car = serializers.BooleanField(required=False)
    has_home = serializers.BooleanField(required=False)
    property = serializers.IntegerField(required=False)
    income = serializers.IntegerField(required=False)
    in_seoul = serializers.BooleanField(required=False)
    children = serializers.BooleanField(required=False)
    budget = serializers.IntegerField(required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'nickname': self.validated_data.get('nickname', ''),
            'gender': self.validated_data.get('gender', ''),
            'age': self.validated_data.get('age', ''),
            'phone': self.validated_data.get('phone', ''),
            'has_car': self.validated_data.get('has_car', False),
            'has_home': self.validated_data.get('has_home', False),
            'property': self.validated_data.get('property', 0),
            'income': self.validated_data.get('income', 0),
            'in_seoul': self.validated_data.get('in_seoul', False),
            'children': self.validated_data.get('children', False),
            'budget': self.validated_data.get('budget', 0),
        })
        return data

    def save(self, request):
        user = super().save(request)
        user.nickname = self.cleaned_data.get('nickname')
        user.gender = self.cleaned_data.get('gender')
        user.age = self.cleaned_data.get('age')
        user.phone = self.cleaned_data.get('phone')
        user.has_car = self.cleaned_data.get('has_car')
        user.has_home = self.cleaned_data.get('has_home')
        user.property = self.cleaned_data.get('property')
        user.income = self.cleaned_data.get('income')
        user.in_seoul = self.cleaned_data.get('in_seoul')
        user.children = self.cleaned_data.get('children')
        user.budget = self.cleaned_data.get('budget')
        user.save()
        return user

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        extra_fields = []
        if hasattr(User, 'USERNAME_FIELD'):
            extra_fields.append(User.USERNAME_FIELD)
        if hasattr(User, 'EMAIL_FIELD'):
            extra_fields.append(User.EMAIL_FIELD)
        if hasattr(User, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(User, 'age'):
            extra_fields.append('age')
        if hasattr(User, 'gender'):
            extra_fields.append('gender')
        if hasattr(User, 'phone'):
            extra_fields.append('phone')
        if hasattr(User, 'has_car'):
            extra_fields.append('has_car')
        if hasattr(User, 'has_home'):
            extra_fields.append('has_home')
        if hasattr(User, 'property'):
            extra_fields.append('property')
        if hasattr(User, 'income'):
            extra_fields.append('income')
        if hasattr(User, 'in_seoul'):
            extra_fields.append('in_seoul')
        if hasattr(User, 'children'):
            extra_fields.append('children')
        if hasattr(User, 'budget'):
            extra_fields.append('budget')
        
        model = User
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)