from cpf_field.models import CPFField
from django.db import models
from localflavor.br.models import BRCNPJField, BRPostalCodeField
from phone_field import PhoneField


class Tb_estoque(models.Model):
    id_estoque = models.IntegerField(primary_key=True, verbose_name='Id do estoque')
    id_produto = models.IntegerField(verbose_name='Código do prodúto', null=True)
    ds_n = models.CharField(max_length=45, verbose_name='Nome')
    tamanhoCHOICES = [
        ('PP', 'PP'),
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
    ]
    ds_tamanho = models.CharField(max_length=2, verbose_name='Tamanho', null=True, choices= tamanhoCHOICES)
    corCHOICES = [
        ('Branco', 'Branco'),
        ('Preto', 'Preto'),
        ('Verde', 'Verde'),
        ('Rosa', 'Rosa'),
        ('Vermelho', 'Vermelho'),
    ]
    ds_cor = models.CharField(max_length=10, verbose_name='Cor', null=True, choices=corCHOICES)
    vl_preco_custo = models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Custo',null=True)
    vl_preco_venda = models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Preço de venda', null=True)
    dt_entrada = models.DateField(verbose_name='Data de entrada', null=True)

    class Meta:
        ordering = ('ds_n',)
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoque'

    def __str__(self):
        return self.ds_n

class Tb_cor(models.Model):
    cor = models.CharField(max_length=45)

class Tb_cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = CPFField('cpf')
    cep = BRPostalCodeField(null=True, verbose_name='Cep')
    email = models.EmailField(null=True, verbose_name='Email')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    uf = models.CharField(max_length=2, verbose_name='Uf')
    dt_nascimento = models.DateField(verbose_name='Data de nascimento')

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

class Tb_usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = CPFField('cpf')
    cep = BRPostalCodeField(null=True, verbose_name='Cep')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    email = models.EmailField()
    telefone = PhoneField(blank=True, help_text='Número de contato')
    dt_nascimento = models.DateField(verbose_name='Data de nascimento')

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome

class Tb_fornecedor(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cnpj = BRCNPJField(null=True, blank=True)
    cep = BRPostalCodeField(null=True, verbose_name='Cep')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    email = models.EmailField()
    telefone = PhoneField(blank=True, help_text='Número de contato')
    codigo = models.IntegerField(verbose_name='Código do prodúto')
    proChoices = [
        ('Blusa', 'Blusa'),
        ('Saia', 'Saia'),
        ('Calça', 'Calça'),
        ('Moletom', 'Moletom'),
        ('Bone', 'Bone'),
    ]
    tipo = models.CharField(max_length=45, verbose_name='Tipo do prodúto', choices=proChoices)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome

class Cart(models.Model):
    usuario = models.ForeignKey(Tb_usuario, on_delete=models.DO_NOTHING, verbose_name="Usuário")
    cliente = models.ForeignKey(Tb_cliente, on_delete=models.DO_NOTHING,)
    produto = models.ForeignKey(Tb_estoque, on_delete=models.DO_NOTHING, verbose_name="Prodúto")
    tamanhoCHOICES = [
        ('PP', 'PP'),
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
    ]
    tamanho = models.CharField(max_length=2, verbose_name='Tamanho', null=True, choices=tamanhoCHOICES)
    corCHOICES = [
        ('Branco', 'Branco'),
        ('Preto', 'Preto'),
        ('Verde', 'Verde'),
        ('Rosa', 'Rosa'),
        ('Vermelho', 'Vermelho'),
    ]
    cor = models.CharField(max_length=10, verbose_name='Cor', null=True, choices=corCHOICES)
    newV = models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Preço da venda', null=True)

    class Meta:
        verbose_name = ('Carrinho')
        verbose_name_plural = 'Carrinho'
