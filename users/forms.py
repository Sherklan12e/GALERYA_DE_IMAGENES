from django.contrib.auth.forms import UserCreationForm 
from django.forms.widgets import ClearableFileInput
from .models import User
from django import forms
from .models import Image
from django.core.exceptions import ValidationError


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
            
        self.fields['email'].widget.attrs['class'] = 'w-full p-3 rounded dark:bg-gray-800'
        self.fields['username'].widget.attrs['class'] = 'w-full p-3 rounded dark:bg-gray-800'
        self.fields['password1'].widget.attrs['class'] = 'w-full p-3 rounded dark:bg-gray-800'
        self.fields['password2'].widget.attrs['class'] = 'w-full p-3 rounded dark:bg-gray-800'
            
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
        


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'appearance-none border pl-12 border-gray-100 shadow-sm focus:shadow-md focus:placeholder-gray-600  transition  rounded-md w-full py-3 text-gray-600 leading-tight focus:outline-none focus:ring-gray-600 focus:shadow-outline',
                'style': 'background-image: url(\'/static/images/imas.png\'); background-repeat: no-repeat; background-size: 2.5rem;',
                'id': 'image',
                'accept': 'image/*'
            }
        ),
    )

    # Agrega la etiqueta label con la imagen SVG como fondo
    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full p-3 rounded dark:bg-gray-800',
                'style': '',
            }
        ),
    )
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.endswith('.jpg') and not image.name.endswith('.png'):
                raise ValidationError("Solo se permiten archivos con extensión jpg y png.")
            return image
        else:
            raise ValidationError("No se pudo leer el archivo.")



