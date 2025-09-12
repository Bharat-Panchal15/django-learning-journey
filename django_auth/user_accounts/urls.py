from django.urls import path
from . import views

urlpatterns = [
    path("signup/",views.sign_up,name="sign_up"),
    path("login/",views.login_view,name="log_in"),
    path("logout/",views.logout_view,name="log_out"),
    path("",views.home,name="home"),
]