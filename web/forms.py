from django import forms
from .models import Tb_cliente, Tb_usuario, Tb_fornecedor, Tb_estoque, Cart


class TbProdutoForm(forms.ModelForm):
    class Meta:
        model = Tb_estoque
        required = False
        fields = ('ds_n', 'id_produto', 'ds_tamanho', 'ds_cor', 'vl_preco_custo', 'vl_preco_venda', 'dt_entrada')

class TbClienteForm(forms.ModelForm):
    class Meta:
        model = Tb_cliente
        required = False
        fields = ('nome', 'cpf', 'cep', 'email', 'endereco',  'bairro', 'uf', 'dt_nascimento')

class TbUsuarioForm(forms.ModelForm):
    class Meta:
        model = Tb_usuario
        fields = ('nome', 'cpf', 'cep', 'endereco', 'email', 'telefone', 'dt_nascimento')

class TbFornecedorForm(forms.ModelForm):
    class Meta:
        model = Tb_fornecedor
        fields = ('nome', 'cnpj', 'cep', 'endereco', 'email', 'telefone', 'codigo', 'tipo')


class Cart(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('usuario', 'cliente', 'produto', 'tamanho', 'cor', 'newV')