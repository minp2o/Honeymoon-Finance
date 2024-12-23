

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(blank=True, error_messages={'unique': '닉네임이 중복되었습니다.'}, max_length=30, null=True, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('M', '남성'), ('F', '여성')], max_length=10, null=True)),
                ('age', models.IntegerField(error_messages={'invalid': '제대로 입력하세요.'}, validators=[django.core.validators.MinValueValidator(1, message='나이는 0보다 커야 합니다.'), django.core.validators.MaxValueValidator(120, message='잘못 입력하였습니다.')])),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex='^010-\\d{4}-\\d{4}$')])),
                ('has_car', models.BooleanField(default=False)),
                ('has_home', models.BooleanField(default=False)),
                ('property', models.BigIntegerField(default=False, help_text='재산 (단위: 원)', validators=[django.core.validators.MinValueValidator(0)])),
                ('income', models.BigIntegerField(default=False, help_text='연간 소득 (단위: 원)', validators=[django.core.validators.MinValueValidator(0)])),
                ('in_seoul', models.BooleanField(default=False, help_text='서울 거주 여부')),
                ('children', models.BooleanField(default=False, help_text='3년 이내 자녀 계획')),
                ('budget', models.BigIntegerField(default=False, help_text='예산 (단위: 원)', validators=[django.core.validators.MinValueValidator(0)])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
