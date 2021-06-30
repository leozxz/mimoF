# Generated by Django 3.2.3 on 2021-06-17 19:13

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion
import localflavor.br.models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('cep', localflavor.br.models.BRPostalCodeField(max_length=9, null=True, verbose_name='Cep')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('uf', models.CharField(max_length=2, verbose_name='Uf')),
                ('dt_nascimento', models.DateField(verbose_name='Data de nascimento')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Tb_cor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tb_estoque',
            fields=[
                ('id_estoque', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id do estoque')),
                ('id_produto', models.IntegerField(null=True, verbose_name='Código do prodúto')),
                ('ds_n', models.CharField(max_length=45, verbose_name='Nome')),
                ('ds_tamanho', models.CharField(choices=[('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')], max_length=2, null=True, verbose_name='Tamanho')),
                ('ds_cor', models.CharField(choices=[('Branco', 'Branco'), ('Preto', 'Preto'), ('Verde', 'Verde'), ('Rosa', 'Rosa'), ('Vermelho', 'Vermelho')], max_length=10, null=True, verbose_name='Cor')),
                ('vl_preco_custo', models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Custo')),
                ('vl_preco_venda', models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Preço de venda')),
                ('dt_entrada', models.DateField(null=True, verbose_name='Data de entrada')),
            ],
            options={
                'verbose_name': 'Estoque',
                'verbose_name_plural': 'Estoque',
                'ordering': ('ds_n',),
            },
        ),
        migrations.CreateModel(
            name='Tb_fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cnpj', localflavor.br.models.BRCNPJField(blank=True, max_length=18, null=True)),
                ('cep', localflavor.br.models.BRPostalCodeField(max_length=9, null=True, verbose_name='Cep')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('email', models.EmailField(max_length=254)),
                ('telefone', phone_field.models.PhoneField(blank=True, help_text='Número de contato', max_length=31)),
                ('codigo', models.IntegerField(verbose_name='Código do prodúto')),
                ('tipo', models.CharField(choices=[('Blusa', 'Blusa'), ('Saia', 'Saia'), ('Calça', 'Calça'), ('Moletom', 'Moletom'), ('Bone', 'Bone')], max_length=45, verbose_name='Tipo do prodúto')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Tb_usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('cep', localflavor.br.models.BRPostalCodeField(max_length=9, null=True, verbose_name='Cep')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('email', models.EmailField(max_length=254)),
                ('telefone', phone_field.models.PhoneField(blank=True, help_text='Número de contato', max_length=31)),
                ('dt_nascimento', models.DateField(verbose_name='Data de nascimento')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(choices=[('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')], max_length=2, null=True, verbose_name='Tamanho')),
                ('cor', models.CharField(choices=[('Branco', 'Branco'), ('Preto', 'Preto'), ('Verde', 'Verde'), ('Rosa', 'Rosa'), ('Vermelho', 'Vermelho')], max_length=10, null=True, verbose_name='Cor')),
                ('newV', models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Preço da venda')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='web.tb_cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='web.tb_estoque', verbose_name='Prodúto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='web.tb_usuario', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Carrinho',
                'verbose_name_plural': 'Carrinho',
            },
        ),
    ]
