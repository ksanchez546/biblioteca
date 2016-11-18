from django import forms
from .models import Libro

class PostForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ('ISBN','title','author','editorial','pais','anio',)
