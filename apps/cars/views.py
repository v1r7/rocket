from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from apps.cars.models import CarDetail, SubmitApplication, Auction
from apps.cars.serializers import CarDetailSerializer, SubmitApplicationSerializer, AuctionSerializer


class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser)
    serializer_class = CarDetailSerializer
    queryset = CarDetail.objects.all()


class CarListApiView(generics.ListAPIView):
    permission_classes = (IsAuthenticated)
    queryset = CarDetail.objects.all()


class SubmitApplicationCreateModelMixin(generics.CreateAPIView):
    permission_classes = AllowAny
    serializer_class = SubmitApplicationSerializer
    queryset = SubmitApplication.objects.all()

class AuctionCreateModelMixin(generics.CreateAPIView):
    permission_classes = (IsAdminUser)
    serializer_class = AuctionSerializer
    queryset = Auction.objects.all()


class AuctionListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Auction.objects.all()
