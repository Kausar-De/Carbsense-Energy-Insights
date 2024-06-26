# Generated by Django 4.2.3 on 2024-02-20 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('Wall', 'Wall'), ('Roof', 'Roof'), ('Floor', 'Floor'), ('Fenestration', 'Fenestration'), ('Structural', 'Structural')], default='Wall', max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('unit', models.TextField(choices=[('kg (Kilogram)', 'kg (Kilogram)'), ('l (Litre)', 'l (Litre)'), ('cu.m (Cubic Metre)', 'cu.m (Cubic Metre)'), ('kWh (KiloWatt-Hours)', 'kWh (KiloWatt-Hours)')], default='Choose Unit...', max_length=200, null=True)),
                ('gwp', models.DecimalField(decimal_places=6, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('2.5BHK', '2.5BHK'), ('3BHK', '3BHK'), ('4BHK+', '4BHK+')], default='Choose BHK...', max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('area', models.IntegerField(default=0, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
