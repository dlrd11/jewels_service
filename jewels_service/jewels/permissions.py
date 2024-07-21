from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if type(request.user) is dict:
            return request.user and request.user.get('username')
        return request.user and request.user.is_authenticated
