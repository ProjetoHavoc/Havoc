
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms import ModelForm
from .models import Post, Comentario
import requests


#formulario gerado automaticamente para o model post quando o metodo PostForm for chamado

class PostForm(forms.ModelForm):
    class Meta:
        #indica qual model pertence esse form
        model = Post

        # indica os campos que vão aparecer no forme quando o metodo for chamado
        fields = ['titulo_post', 'excerto_post', 'conteudo_post', 'autor_post', 'categoria_post', 'imagem_post', 'publicado_post']

        #indica os tipos de campo que serão chamados
        widgets = {
            
            'titulo_post': forms.TextInput(attrs={'placeholder':'Titulo', 'class': 'form-control form-control-lg'}),
            'excerto_post': forms.TextInput(attrs={'placeholder':'Súmario', 'class': 'form-control form-control-lg'}),
            'conteudo_post':SummernoteWidget(),
            'autor_post': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            'categoria_post': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            'imagem_post': forms.FileInput(attrs={'id':'validatedCustomFile'}),
            'publicado_post': forms.CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            
        }
#formulario gerado automaticamente para o model Comentario quando o metodo FormComentario for chamado

class FormComentario(ModelForm):

    #redefinindo o metodo
    def clean(self):

        #declaarando as variaveis para autenticação do Recapcha
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')
        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LdmuVgdAAAAAJ9oVtnNSmYLwwSRjQhWSA2KUOP2', # secret key do google recapcha
                'response': recaptcha_response                        # variavel que recebe a requisicao do fronte 
            }
        )

        recaptcha_result = recaptcha_request.json()

        print(recaptcha_result)
        
        print(recaptcha_result.get('success'))


        

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais que 5 caracteres.'
            )

        #Mensagem de erro caso o recapcha não for correspondente
        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe, o reCAPCHA não correnponde.'
            )    

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
