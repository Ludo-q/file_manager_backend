from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from knox.views import LoginView as KnoxLoginView

from .models import UserFileManager
from .serializers import UserFileManagerSerializer, PermissionSerializer
from .permissions import IsOwnerOrReadOnly


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []

    def post(self, request, format=None):

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class UserFileManagerListView(APIView):
    """
    List all users or create a new user
    """

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request):
        users = UserFileManager.objects.all()
        serializer = UserFileManagerSerializer(users, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = UserFileManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'error': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class PermissionListView(APIView):
    """
    List all permission or create a new permission.

    The new permission is created only in relation of `UserFileManager` model
    as a `content_type`
    """

    def get(self, request):
        django_permissions = Permission.objects.all()
        serializer = PermissionSerializer(django_permissions, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        codename = request.data['codename']
        name = request.data['name']
        content_type = ContentType.objects.get_for_model(UserFileManager)

        data = {
            'codename': codename,
            'name': name,
            'content_type': content_type.pk
        }

        serializer = PermissionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'A new permission is created', 'created_permission': serializer.data},
                status.HTTP_201_CREATED
            )

        return Response(
            {'error': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
