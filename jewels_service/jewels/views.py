from rest_framework import generics, permissions
from .models import Jewel
from .serializers import JewelSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .utils import verify_token

class JewelListCreateView(generics.ListCreateAPIView):
    queryset = Jewel.objects.all()
    serializer_class = JewelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            token = self.request.headers.get('Authorization', '').split('Bearer ')[-1]
            if token and verify_token(token):
                self.permission_classes = [permissions.IsAuthenticated]
            else:
                self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()

class JewelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jewel.objects.all()
    serializer_class = JewelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            token = self.request.headers.get('Authorization', '').split('Bearer ')[-1]
            if token and verify_token(token):
                self.permission_classes = [permissions.IsAuthenticated]
            else:
                self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()
