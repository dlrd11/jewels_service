from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response

from .authentication import CustomJWTAuthentication
from .models import Jewel
from .permissions import CustomAuthenticatedOrReadOnly
from .serializers import JewelSerializer


class JewelView(generics.ListCreateAPIView):
    queryset = Jewel.objects.all()
    serializer_class = JewelSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [CustomAuthenticatedOrReadOnly]
    authentication_classes = [CustomJWTAuthentication]

    @swagger_auto_schema(
        operation_description="Retrieve all jewels",
        responses={200: JewelSerializer(many=True)},
    )
    def get(self, request, pk=None, *args, **kwargs):

        if not pk:
            return self.list(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new jewel",
        request_body=JewelSerializer,
        responses={201: JewelSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
