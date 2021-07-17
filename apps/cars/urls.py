from django.urls import path

from apps.cars.views import CarRetrieveUpdateDestroyAPIView, CarListApiView, SubmitApplicationCreateModelMixin, \
    AuctionCreateModelMixin, AuctionListView

urlpatterns = [
    path('car/', CarRetrieveUpdateDestroyAPIView.as_view(), name='api_car'),
    path('cars/', CarListApiView.as_view(), name='car_view'),
    path('application/',
         SubmitApplicationCreateModelMixin.as_view(), name='submitapplication'),
    path('auction/',
         AuctionCreateModelMixin.as_view(), name='create_auction_api'),
    path('auctionview/',
         AuctionListView.as_view(), name='api_auction'),

]