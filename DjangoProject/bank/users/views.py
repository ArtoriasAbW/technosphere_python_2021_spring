from rest_framework import viewsets
from users.serializers import CustomUserSerializer
from users.models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


