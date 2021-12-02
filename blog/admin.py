from django.contrib import admin
from .models import Post, Categoria, Comentario
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

# registrando no admin com summernote
class PostAdmin(SummernoteModelAdmin):

    list_display = ('id','titulo_post', 'autor_post', 'data_post', 
                    'categoria_post','publicado_post',)

    list_editable = ('publicado_post',)

    list_display_links = ('id', 'titulo_post',)

    summernote_fields = ('conteudo_post', )


# deixando os campos disponiveis no admin
class ComentarioAdmin(admin.ModelAdmin):

    list_display = ('id', 'nome_comentario', 'email_comentario', 
                    'post_comentario', 'data_comentario',
                    'publicado_comentario', )

    list_editable = ('publicado_comentario', )

    list_display_links = ('id', 'nome_comentario', 'email_comentario', )    

# deixando os campos disponiveis no admin
class CategoriaAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nome_categoria')
    list_display_links = ('id', 'nome_categoria')

       

# registrando no admin
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Categoria, CategoriaAdmin) 
