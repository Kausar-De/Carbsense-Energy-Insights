# Generated by Django 4.2.3 on 2024-02-20 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_floorassembly_roofassembly_wallassembly_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='date_added',
        ),
    ]
