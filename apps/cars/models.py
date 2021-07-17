from django.db import models

from core import settings
from utils.upload import upload_instance


class CarDetail(models.Model):
    """Детальная Модель Машины"""
    article = models.CharField(verbose_name='Артикул', max_length=255)
    name = models.CharField(verbose_name='Марка', max_length=255)
    status = models.CharField(verbose_name="Состояние", max_length=255)
    production_date = models.SmallIntegerField(verbose_name="Год выпуска", default=2000)
    picture = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_instance)
    started_price = models.SmallIntegerField(verbose_name="Начальная цена", default=0)
    data_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Обзор машины'
        verbose_name_plural = 'Обзор машин'

    def __str__(self):
        return self.name

class SubmitApplication(models.Model):
    """Форма заявки"""
    name = models.CharField(verbose_name="Имя", max_length=255)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20)
    picture = models.ImageField(upload_to=upload_instance, verbose_name='Фото машины')
    data_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name


class Auction(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Участник')
    car = models.ForeignKey(CarDetail, on_delete=models.CASCADE, verbose_name='Машина')
    price_after_step_up = models.CharField(verbose_name='Цена после повышения', max_length=255)
        # f'{started_price}+{step_up_price}'
    step_up_price = models.CharField(verbose_name='Цена повышения', max_length=255)
    finished_price = models.CharField(verbose_name='Цена продажи', max_length=255)
        # f'{price_after_step_up}'
    in_progress = models.BooleanField(default=False, verbose_name='Текущий аукцион')
    finished = models.BooleanField(default=False, verbose_name='Завершенный аукцион')

    class Meta:
        verbose_name = 'Аукцион'
        verbose_name_plural = 'Аукционы'

    def __str__(self):
        return self.customer

