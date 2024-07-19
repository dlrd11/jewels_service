from rest_framework import generics, permissions, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .authentication import CustomJWTAuthentication
from .models import Jewel
from .permissions import CustomAuthenticatedOrReadOnly
from .serializers import JewelSerializer
from .utils import verify_token


class JewelView(generics.ListCreateAPIView):
    queryset = Jewel.objects.all()
    serializer_class = JewelSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [CustomAuthenticatedOrReadOnly]
    authentication_classes = [CustomJWTAuthentication]

    def get(self, request, pk=None, *args, **kwargs):

        if not pk:
            return self.list(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
