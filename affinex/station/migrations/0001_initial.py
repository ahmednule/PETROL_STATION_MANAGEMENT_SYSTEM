# Generated by Django 5.0.6 on 2024-08-06 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rfid_tag', models.CharField(max_length=50)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.fuelstation')),
            ],
        ),
        migrations.AddField(
            model_name='fuelstation',
            name='fuel_types',
            field=models.ManyToManyField(to='station.fueltype'),
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_level', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.fueltype')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.fuelstation')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.fueltype')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.fuelstation')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(max_length=50)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.transaction')),
            ],
        ),
    ]