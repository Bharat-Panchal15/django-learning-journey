from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_post,name='home'),
    path('create/',views.create_post,name='create_post'),
    path('contact/',views.contact_view,name='contact'),
]