# Generated by Django 4.2.3 on 2024-02-20 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_remove_building_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
