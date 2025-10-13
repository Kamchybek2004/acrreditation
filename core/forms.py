from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

def validate_latin_password(value):
    if not re.match(r'^[A-Za-z0-9@#$%^&+=!_-]+$', value):
        raise ValidationError(
            "Пароль может содержать только латинские буквы, цифры и символы @ # $ % ^ & + = ! _ -."
        )
    if not re.search(r'[A-Z]', value):
        raise ValidationError("Пароль должен содержать хотя бы одну заглавную латинскую букву.")
    if not re.search(r'[0-9]', value):
        raise ValidationError("Пароль должен содержать хотя бы одну цифру.")


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Электронная почта",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "username@gmail.com"
        })
    )

    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите имя пользователя"
        })
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Введите пароль"
        }),
        validators=[validate_latin_password]
    )

    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Повторите пароль"
        }),
        validators=[validate_latin_password]
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите логин"
        })
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Введите пароль"
        })
    )
