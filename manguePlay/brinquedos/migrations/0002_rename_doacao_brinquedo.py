# Generated by Django 5.1.2 on 2024-10-16 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brinquedos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doacao',
            new_name='Brinquedo',
        ),
    ]