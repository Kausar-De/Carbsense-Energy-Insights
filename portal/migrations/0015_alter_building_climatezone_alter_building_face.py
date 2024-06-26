# Generated by Django 4.2.3 on 2024-03-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_alter_buildingsystems_appls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='climatezone',
            field=models.TextField(choices=[('Hot & Dry', 'Hot & Dry'), ('Composite', 'Composite'), ('Warm & Humid', 'Warm & Humid'), ('Temperate', 'Temperate'), ('Cold', 'Cold')], default='Choose Climate Zone...', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='face',
            field=models.TextField(choices=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West'), ('North-East', 'North-East'), ('North-West', 'North-West'), ('South-East', 'South-East'), ('South-West', 'South-West')], default='Choose Face Direction...', max_length=200, null=True),
        ),
    ]
