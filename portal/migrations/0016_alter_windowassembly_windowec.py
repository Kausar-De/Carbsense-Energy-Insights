# Generated by Django 4.2.3 on 2024-04-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_alter_building_climatezone_alter_building_face'),
    ]

    operations = [
        migrations.AlterField(
            model_name='windowassembly',
            name='windowec',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
