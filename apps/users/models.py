from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from core import settings


class UserManager(BaseUserManager):
    """Модель Админа"""

    def create_user(self, phone_number, email=None, password=None):
        if not phone_number:
            raise ValueError("Users must have a Phone number")
        email = UserManager.normalize_email(email)

        user = self.model(phone_number=phone_number, email=email,
                          is_staff=False, is_active=True, is_superuser=False, )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Модель Пользователей"""
    first_name = models.CharField(verbose_name='Имя, Фамилия', max_length=255)
    email = models.EmailField(verbose_name='Почта', max_length=60,)
    date_joined = models.DateTimeField(verbose_name='Дата/время регистрации',
                                       auto_now_add=True)
    phone_number = models.SmallIntegerField(verbose_name='Номер телефона', unique=True,
                                            default=0)
    last_login = models.DateTimeField(verbose_name='Последний вход',
                                      auto_now=True)
    action = models.CharField(verbose_name='Аукционов сыграно', max_length=255, blank=True)
    action_wins = models.CharField(verbose_name='Аукционов выйграно', max_length=255, blank=True)
    check_accepted = models.BooleanField(verbose_name='Подтверждение регистрации', default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.first_name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)