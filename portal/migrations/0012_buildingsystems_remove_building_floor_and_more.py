# Generated by Django 4.2.3 on 2024-03-20 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_building_acctype_building_address_building_face_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingSystems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hvacsystem', models.TextField(choices=[('Fan', 'Fan'), ('Split AC', 'Split AC'), ('Window AC', 'Window AC'), ('Split + Window AC', 'Split + Window AC'), ('Mixed Mode/Hybrid', 'Mixed Mode/Hybrid'), ('Evaporative Cooler', 'Evaporative Cooler'), ('VRF', 'VRF')], default='Choose Primary HVAC System...', max_length=200, null=True)),
                ('starrating', models.TextField(choices=[('1 Star', '1 Star'), ('2 Star', '2 Star'), ('3 Star', '3 Star'), ('4 Star', '4 Star'), ('5 Star', '5 Star')], default='Choose Star Rating...', max_length=200, null=True)),
                ('setpoint', models.IntegerField(default=0, null=True)),
                ('totaltr', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='building',
            name='floor',
        ),
        migrations.AddField(
            model_name='building',
            name='billamt',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='lastyr_units',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='occupants',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='threeyrbfr_units',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='twoyrbfr_units',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='units',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='yourfloor',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='buildingsystems',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.buildingsystems'),
        ),
    ]
