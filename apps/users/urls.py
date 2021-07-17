from django.urls import path

from apps.users.views import UserAuthView, UsersListAPIView

urlpatterns = [
    path('auth', UserAuthView.as_view(), name='auth'),
    path('users', UsersListAPIView.as_view(), name='users_list'),

]