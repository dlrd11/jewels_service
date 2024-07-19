from rest_framework import exceptions
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework_simplejwt.authentication import JWTAuthentication

from .utils import verify_token


class CustomJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        # validated_token = self.get_validated_token(raw_token)
        user_data = self.verify_external_token(raw_token)

        return user_data, raw_token

    def verify_external_token(self, raw_token):
        breakpoint()
        try:
            user_data = verify_token(raw_token)
            return user_data
        except exceptions.AuthenticationFailed:
            raise exceptions.AuthenticationFailed('Token is invalid or expired')


class AllowAny(BasePermission):
    """
    Custom permission to allow only authenticated users for write actions.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
