from rest_framework import permissions

class IsAuthorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:   ## 읽기 권한 모든 사용자에게
            return True
        
        # 작성자이거나 관리자인 경우 CUD 권한을 부여
        return obj.author == request.user or request.user.is_staff
