from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
        

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome")
    email = forms.EmailField(max_length=100, label="E-mail")
    telefone = forms.CharField(max_length=15, label="Telefone")