# Generated by Django 4.1.2 on 2022-10-16 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familiar',
            old_name='direccion',
            new_name='nacimiento',
        ),
        migrations.RenameField(
            model_name='familiar',
            old_name='numero_pasaporte',
            new_name='numero_documento',
        ),
    ]
