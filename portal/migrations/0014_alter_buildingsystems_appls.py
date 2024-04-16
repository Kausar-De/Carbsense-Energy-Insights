# Generated by Django 4.2.3 on 2024-03-25 08:33

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_buildingsystems_appls_buildingsystems_otherappls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingsystems',
            name='appls',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Air Conditioner', 'Air Conditioner'), ('Computer', 'Computer'), ('LED', 'LED'), ('CFL', 'CFL'), ('Microwave', 'Microwave'), ('Washing Machine', 'Washing Machine'), ('Ceiling Fan', 'Ceiling Fan'), ('Refrigerator', 'Refrigerator'), ('Air Fryer', 'Air Fryer'), ('Chimney', 'Chimney'), ('Geyser', 'Geyser'), ('OTG', 'OTG'), ('Oven', 'Oven'), ('Electric Stove', 'Electric Stove'), ('BEV Charger', 'BEV Charger'), ('Television', 'Television'), ('Room Heater', 'Room Heater'), ('Electric Kettle', 'Electric Kettle'), ('Other', 'Other')], max_length=200, null=True),
        ),
    ]