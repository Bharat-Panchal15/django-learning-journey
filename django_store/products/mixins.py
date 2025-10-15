from django.contrib.auth.mixins import UserPassesTestMixin

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_staff
    
    def handle_no_permission(self):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("You are not authorized to perform this action.")