# Generated by Django 5.1.2 on 2024-10-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_doador', models.CharField(max_length=100)),
                ('contato', models.CharField(max_length=15)),
                ('local', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fim', models.TimeField()),
                ('observacoes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
