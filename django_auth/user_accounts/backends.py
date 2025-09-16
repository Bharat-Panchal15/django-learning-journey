from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class IdentityBackend(BaseBackend):
    def authenticate(self, request, identity=None, password=None, **kwargs):
        print("Trying to authenticate:",identity,password)
        try:
            user = User.objects.get(Q(username=identity) | Q(email=identity))
        
        except User.DoesNotExist:
            print("No user found with that identity")
            return None
        
        if user.check_password(password):
            print("Authentication successful")
            return user
        else:
            print("Password Incorrect")
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None