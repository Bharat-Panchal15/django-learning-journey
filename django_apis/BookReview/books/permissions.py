from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Allow full access to the object's owner
    but read-only access to everyone else."""

    def has_object_permission(self, request, view, obj):
        # Anyone can read (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True
        # Write permissions only for the review's author
        return obj.user == request.user