# Generated by Django 4.1.3 on 2023-02-03 00:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('cpf', django_cpf_cnpj.fields.CPFField(max_length=14, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': [('CD', 'Cadastrar,Apagar'), ('RU', 'Lerd,Atualizar')],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cnpj', django_cpf_cnpj.fields.CNPJField(max_length=18)),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('codigoPostal', models.IntegerField(verbose_name='CEP')),
                ('emailFornecedor', models.EmailField(max_length=100, verbose_name='Email')),
                ('fotoFornecedor', models.ImageField(null=True, upload_to='fornecedoresImg', verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30, verbose_name='Nome')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('fotoUm', models.ImageField(upload_to='fotosProduto', verbose_name='Foto')),
                ('fotoDois', models.ImageField(blank=True, upload_to='fotosProduto', verbose_name='Foto')),
                ('fotoTres', models.ImageField(blank=True, upload_to='fotosProduto', verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Retiradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidaderet', models.IntegerField(verbose_name='Quantidade')),
                ('data', models.DateTimeField(default='2016-01-01 01:00:00 +00:00')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.produto')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='equipamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoproduto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fornecedor'),
        ),
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidadeent', models.IntegerField(verbose_name='Quantidade')),
                ('data', models.DateTimeField(default='2016-01-01 01:00:00 +00:00')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.produto')),
            ],
        ),
    ]
