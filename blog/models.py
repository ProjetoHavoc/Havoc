from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os

# model de categoria
class Categoria(models.Model):

    nome_categoria = models.CharField(max_length=50)
    
    #metodo que retorma um nome para a classe
    def __str__(self):
        return self.nome_categoria  

# model de post
class Post(models.Model):

    titulo_post = models.CharField(max_length=255, verbose_name='Titulo')
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data da Publicação')
    conteudo_post = models.TextField(verbose_name='Conteúdo')
    excerto_post = models.TextField(verbose_name='Sumário')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Categoria')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=False, null=False, verbose_name='Imagem')
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado')

    #metodo que retorma um nome para a classe
    def __str__(self):
        return self.titulo_post   


# model de comentario
class Comentario(models.Model):

    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_comentario = models.DateTimeField(default=timezone.now) #lembrar de declarar timezone lá em cima
    publicado_comentario = models.BooleanField(default=False) 

    #metodo que retorma um nome para a classe    
    def __str__(self):
        return self.nome_comentario    