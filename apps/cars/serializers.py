from rest_framework import serializers

from apps.cars.models import CarDetail, SubmitApplication, Auction


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDetail
        fields = ['slug', 'name', 'status', 'year', 'picture', 'start_price', 'finish_price', 'data_created']


class CarLastestViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDetail
        fields = ['picture']



class SubmitApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitApplication
        fields = ['name', 'phone_number', 'picture']



class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['customer', 'car', 'price_after_step_up',
                  'step_up_price', 'finished_price', 'in_progress', 'finished']

