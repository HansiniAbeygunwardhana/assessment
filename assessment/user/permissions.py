from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS