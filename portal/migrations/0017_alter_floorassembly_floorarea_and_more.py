# Generated by Django 4.2.3 on 2024-04-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_alter_windowassembly_windowec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorassembly',
            name='floorarea',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='floorassembly',
            name='floorec',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='roofassembly',
            name='roofarea',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='roofassembly',
            name='roofec',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='structuralassembly',
            name='structuralarea',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='structuralassembly',
            name='structuralec',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='wallassembly',
            name='wallarea',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='wallassembly',
            name='wallec',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='windowassembly',
            name='windowarea',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='windowassembly',
            name='windowec',
            field=models.FloatField(default=0, null=True),
        ),
    ]
