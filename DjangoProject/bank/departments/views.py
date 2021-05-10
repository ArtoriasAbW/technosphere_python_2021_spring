
from rest_framework import viewsets
from rest_framework.response import Response

from departments.serializers import DepartmentSerializer
from departments.models import Department
from users.models import CustomUser


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def list(self, request, *args, **kwargs):
        auth_user = request.user
        if not auth_user.is_superuser:
            self.queryset = Department.objects.filter(user=CustomUser.objects.get(username=auth_user))
        serializer = DepartmentSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        pass

    def retrieve(self, request, pk=None, **kwargs):
        pass

    def update(self, request, pk=None, **kwargs):
        pass

    def partial_update(self, request, pk=None, **kwargs):
        pass

    def destroy(self, request, pk=None, **kwargs):
        pass
