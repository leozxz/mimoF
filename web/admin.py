from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry
from . models import Tb_estoque, Tb_cliente, Tb_usuario, Tb_fornecedor, Cart

admin.site.site_header = 'Mimo Store - Consulta'
admin.site.index_title = 'Consulta rapida'



admin.site.unregister(User)
admin.site.unregister(Group)
LogEntry.objects.all().delete()

@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display=('produto', 'tamanho', 'cor',  'newV')
    readonly_fields=('produto', 'usuario', 'cliente')

    def has_add_permission(self, request):
        return False

@admin.register(Tb_usuario)
class Tb_usuarioAdmin(admin.ModelAdmin):
    list_display=('nome', 'cpf',)
    search_fields=('nome',)
    readonly_fields=('cpf', 'cep', 'endereco', 'email', 'dt_nascimento',)

    def has_add_permission(self, request):
        return False


@admin.register(Tb_cliente)
class Tb_clienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf',)
    search_fields=('nome',)
    readonly_fields=('cpf', 'cep', 'email', 'endereco', 'bairro', 'uf', 'dt_nascimento',)

    def has_add_permission(self, request):
        return False

@admin.register(Tb_estoque)
class Tb_estoqueAdmin(admin.ModelAdmin):
    list_display = ('ds_n', 'id_produto','dt_entrada',)
    search_fields=('ds_n',)
    readonly_fields = ('id_estoque', 'id_produto', 'vl_preco_custo', 'vl_preco_venda', 'dt_entrada',)
    date_hierarchy = 'dt_entrada'

    def has_add_permission(self, request):
        return False

@admin.register(Tb_fornecedor)
class Tb_fornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj','tipo',)
    search_fields=('nome',)
    readonly_fields = ('cnpj', 'cep', 'endereco', 'email', 'codigo', 'tipo',)

    def has_add_permission(self, request):
        return False

