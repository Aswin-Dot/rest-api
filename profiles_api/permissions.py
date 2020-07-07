from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    #Allow users to edit their own profile
    def has_object_permission(self, request, view, obj):
        #check user is trying to edit their own profiles
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    #Allow user to update thier own status

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
