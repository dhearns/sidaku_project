from rest_framework import permissions
from rest_framework.permissions import BasePermission
from .models import Detail

class IsUMKMOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_authenticated:
            return False

        try:
            profile = request.user.detail
        except Detail.DoesNotExist:
            return False

        return bool(profile.role == 'umkm')
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_authenticated:
            return False

        try:
            profile = request.user.detail
        except Detail.DoesNotExist:
            return False

        return bool(profile.role == 'umkm')


class IsKoperasiOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_authenticated:
            return False

        try:
            profile = request.user.detail
        except Detail.DoesNotExist:
            return False

        return bool(profile.role == 'koperasi')
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_authenticated:
            return False

        try:
            profile = request.user.detail
        except Detail.DoesNotExist:
            return False

        return bool(profile.role == 'koperasi' and obj.user == request.user)
    
class IsSuperAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_authenticated:
            return False

        try:
            superuser = request.user.is_superuser
            staff = request.user.is_staff
        except Detail.DoesNotExist:
            return False

        return bool(superuser and staff)
    
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        if not request.user.is_authenticated:
            return False

        try:
            superuser = request.user.is_superuser
            staff = request.user.is_staff
        except Detail.DoesNotExist:
            return False

        return bool(superuser and staff)
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
