from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.cars.models import CarDetail, SubmitApplication, Auction


@admin.register(CarDetail)
class CarDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'article',  'status', 'production_date', 'get_image' ]


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="100" height="100"')

    get_image.short_description = "Изображение"

@admin.register(SubmitApplication)
class SubmitApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="100" height="100"')

    get_image.short_description = "Изображение"


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ['customer', ]
