from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, sign_up, login_view, logout_view

urlpatterns = [
    path("",home,name="home"),
    path("signup/",sign_up, name="sign_up"),
    path("login/",login_view,name="log_in"),
    path("logout/",logout_view,name="log_out"),
    path("login_new/",LoginView.as_view(template_name="login_built_in.html"),name="login"),
    path("logout_new/",LogoutView.as_view(next_page="login"),name="logout"),
]