# Generated by Django 4.2.3 on 2024-02-23 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_floorassembly_floorec_roofassembly_roofec_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roofassembly',
            old_name='insulation',
            new_name='roofinsulation',
        ),
        migrations.RenameField(
            model_name='roofassembly',
            old_name='tile',
            new_name='rooftile',
        ),
        migrations.RenameField(
            model_name='wallassembly',
            old_name='insulation',
            new_name='wallinsulation',
        ),
        migrations.RenameField(
            model_name='wallassembly',
            old_name='tile',
            new_name='walltile',
        ),
    ]
