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
    has_car = models.BooleanField(default=False)
    has_home = models.BooleanField(default=False)
    property = models.BigIntegerField(
        default=False,
        validators=[MinValueValidator(0)],
        help_text="재산 (단위: 원)"
    )
    income = models.BigIntegerField(
        default=False,
        validators=[MinValueValidator(0)],
        help_text="연간 소득 (단위: 원)"
    )
    in_seoul = models.BooleanField(default=False, help_text="서울 거주 여부")
    children = models.BooleanField(default=False, help_text="3년 이내 자녀 계획")
    budget = models.BigIntegerField(
        default=False,
        validators=[MinValueValidator(0)],
        help_text="예산 (단위: 원)"
    )