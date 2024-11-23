from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(
        max_length=30, 
        unique=True, 
        null=True, 
        blank=True, 
        error_messages={
            'unique': '닉네임이 중복되었습니다.'
        }
    )
    gender = models.CharField(
        max_length=10, 
        choices=(('M', '남성'), ('F', '여성')), 
        null=True, 
        blank=True
    )
    age = models.IntegerField(
        validators=[
            MinValueValidator(1, message="나이는 0보다 커야 합니다."),
            MaxValueValidator(120, message="잘못 입력하였습니다.")
        ],
        error_messages={
            'invalid': '제대로 입력하세요.',
        }
    )
    phone = models.CharField(
        max_length=13,  
        validators=[
            RegexValidator(
                regex=r'^010-\d{4}-\d{4}$',
            )
        ]
    )