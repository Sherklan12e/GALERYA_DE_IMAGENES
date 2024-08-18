from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.static import serve
from django.http import HttpResponse
from django.http import Http404
from .models import Image
from django.core.exceptions import ObjectDoesNotExist
from .forms import ImageUploadForm
import os
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Visit

@login_required
def some_view(request):
    Visit.objects.create(user=request.user)
    # ... rest of your view code ...

def register_page(request):
    form = RegisterUserForm()
    
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            
            login(request, user)
            messages.success(request, "Account created!")
            return redirect('home')
        else:
            messages.success(request, "a error ocorred during ")
    return render(request, "users/register.html", {'form':form})


def logout_user(request):
    logout(request)
    messages.success(request, "NOS VEMOS DESPUES prrr")
    return redirect("login")



def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.success(request, "User does not exist!")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "WELCOME BACK " + user.email)
            return redirect('home')
        else:
            messages.success(request, "USERNAME OR PASSWORD DOES NOT MATCH!")
            
    return render(request, "users/login.html")






def galeria(request):
    images = Image.objects.all()
    
    return render(request, 'blog/galeria.html', {'images': images})

def subir_imagen(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('galeria')
    else:
        form = ImageUploadForm()
    return render(request, 'blog/subir_imagen.html', {'form': form})

def delete_image(request, id):
    image = get_object_or_404(Image, id=id)
    if request.user != image.user:
        messages.error(request, 'No tiene permiso para eliminar esta imagen.')
        return redirect('galeria')
    if request.method == 'POST':
        imagen_path = image.image.path
        os.remove(imagen_path)
        image.delete()
        messages.success(request, 'La imagen ha sido eliminada.')
        return redirect('galeria')
    return render(request, 'blog/eliminar.html', {'image': image})




def search(request):
    query = request.GET.get('q', '')  # Obtén el parámetro de búsqueda de la URL
    if query:
        # Filtra los locales por nombre, dirección, y descripción usando la búsqueda insensible a mayúsculas/minúsculas
        results = Local.objects.filter(
            nombre__icontains=query
        ) | Image.objects.filter(
            direccion__icontains=query
        ) | Image.objects.filter(
            descripcion__icontains=query
        )
    else:
        results = Image.objects.none()  # Si no hay consulta, no se muestran resultados

    return render(request, 'index.html', {'results': results})


