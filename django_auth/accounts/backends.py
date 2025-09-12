from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class UsernameBackend(BaseBackend):
    def authenticate(self,request, username=None, password=None,**kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        
class EmailBackend(BaseBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        email = kwargs.get("email") or username
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        