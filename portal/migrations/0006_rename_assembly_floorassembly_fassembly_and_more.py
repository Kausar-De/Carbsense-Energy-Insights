# Generated by Django 4.2.3 on 2024-02-20 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_alter_windowassembly_frame'),
    ]

    operations = [
        migrations.RenameField(
            model_name='floorassembly',
            old_name='assembly',
            new_name='fassembly',
        ),
        migrations.RenameField(
            model_name='roofassembly',
            old_name='assembly',
            new_name='rassembly',
        ),
        migrations.RenameField(
            model_name='wallassembly',
            old_name='assembly',
            new_name='wassembly',
        ),
    ]