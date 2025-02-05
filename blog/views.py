from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .forms import ContatoForm
from django.core.mail import send_mail
from django.conf import settings

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']

            # Enviar o e-mail com os dados do contato
            assunto = f'Novo contato recebido: {nome}'
            mensagem = f'Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}'
            remetente = settings.EMAIL_HOST_USER
            destinatario = ['lribeirodossantos095@gmail.com']  # Substitua pelo seu e-mail

            send_mail(assunto, mensagem, remetente, destinatario, fail_silently=False)

            return render(request, 'blog/contato_sucesso.html', {'nome': nome})
    else:
        form = ContatoForm()

    return render(request, 'blog/contato.html', {'form': form})


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']

            # Salvar os dados no banco de dados
            Contato.objects.create(nome=nome, email=email, telefone=telefone)

            return render(request, 'blog/contato_sucesso.html', {'nome': nome, 'email': email, 'telefone': telefone})
    else:
        form = ContatoForm()
    return render(request, 'blog/contato.html', {'form': form})


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Aqui você pode salvar as informações ou enviar um e-mail
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            # Para simplificação, apenas exibe os dados recebidos
            return render(request, 'blog/contato_sucesso.html', {'nome': nome, 'email': email, 'telefone': telefone})
    else:
        form = ContatoForm()
    
    return render(request, 'blog/contato.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})
 
def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})