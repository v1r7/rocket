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
    serializer_class = CarDetailSerializer
    queryset = CarDetail.objects.all().order_by('finished')[:5]


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
    queryset = Auction.objects.filter(customer__user_check_accepted=True).order_by('in_progress')
