from django.views.static import serve
from django.http import HttpResponse
from django.conf import settings
from django.urls import path 
from . views import login_page, register_page, logout_user , galeria , subir_imagen, delete_image
urlpatterns = [
    path("login/", login_page , name="login"),
    path("register/", register_page , name="register"),
    path("logout_page/", logout_user, name="logout_user"),
    path("galeria/",   galeria,name='galeria'),
    path("subir_imagen/",   subir_imagen,name='subir_imagen'),
    path('delete_image/<int:id>/', delete_image, name='delete_image'),
    



    
    
]
