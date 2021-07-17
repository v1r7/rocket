from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import AuthSerializer, UsersListSerializer, UsersCreateSerializer


class UserAuthView(APIView):
    permission_classes = [AllowAny]
    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.allowed_methods
        user = User.objects.filter(phone_number=serializer.data.get('phone_number')).first()

        if user is None:
            return Response(
                data={'error': 'Пользотеватель не найден'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not user.check_password(serializer.data.get('password')):
            return Response(
                data={'error': 'Не верный пароль'},
                status=status.HTTP_404_NOT_FOUND,
            )

        user_token, created = Token.objects.get_or_create(user=user)

        return Response(data={'token': user_token.key}, status=status.HTTP_200_OK)


class UsersListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        self.serializer_class = UsersListSerializer
        return super(UsersListAPIView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = UsersCreateSerializer
        return super(UsersListAPIView, self).post(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(serializer.validated_data.get('password'))
        instance.save()