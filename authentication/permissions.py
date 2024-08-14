from rest_framework.permissions import BasePermission

class IsChild(BasePermission):
    def has_permission(self,request,view):
        if request.user and request.user.child:
            return True
        else:
            return False
        
class IsParent(BasePermission):
    def has_permission(self,request,view):
        if request.user and request.user.parent:
            return True
        else:
            return False