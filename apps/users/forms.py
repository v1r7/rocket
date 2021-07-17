from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    phone_number = forms.CharField(
        label='Номер телефона',
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control input-lg'}),
    )
    password = forms.CharField(
        label='Пароль',
        max_length=128,
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control input-lg'}),
    )

    def clean_email(self):
        phone_number = self.cleaned_data.get('phone_number')

        if not phone_number:
            raise ValidationError('Обязательное поле')

        return phone_number

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not password:
            raise ValidationError('Обязательное поле')

        return password