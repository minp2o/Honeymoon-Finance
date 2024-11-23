from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=30, required=False, allow_blank=True)
    gender = serializers.ChoiceField(choices=[('M', '남성'), ('F', '여성')], required=False, allow_blank=True)
    age = serializers.IntegerField(required=True)
    phone = serializers.CharField(required=True)

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

class CustomUserDetailsSerializer(serializers.ModelSerializer):
       class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
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
        
        
        model = User
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)

        