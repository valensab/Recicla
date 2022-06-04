# Generated by Django 4.0.3 on 2022-03-28 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id_publication', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('type_material', models.CharField(blank=True, max_length=254, null=True, verbose_name='Tipo de material')),
                ('address', models.CharField(blank=True, max_length=30, null=True, verbose_name='Dirección')),
                ('weight', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Peso')),
                ('volume', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Volumen')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Descripción')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('state', models.BooleanField(default=False, verbose_name='Estado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
    ]
