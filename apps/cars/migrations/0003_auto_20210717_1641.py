# Generated by Django 3.2.2 on 2021-07-17 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auction_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={'verbose_name': 'Аукцион', 'verbose_name_plural': 'Аукционы'},
        ),
        migrations.AlterModelOptions(
            name='cardetail',
            options={'verbose_name': 'Обзор машины', 'verbose_name_plural': 'Обзор машин'},
        ),
        migrations.AlterModelOptions(
            name='submitapplication',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]