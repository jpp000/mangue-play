# Generated by Django 5.1.2 on 2024-11-24 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0002_fornecedor_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='email',
        ),
    ]