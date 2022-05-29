# Generated by Django 4.0.2 on 2022-05-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RentVehicle_Date_of_Booking', models.DateField(blank=True, null=True)),
                ('RentVehicle_Date_of_Return', models.DateField(blank=True, null=True)),
                ('Total_days', models.IntegerField()),
                ('Advance_amount', models.IntegerField(blank=True, null=True)),
                ('RentVehicle_Total_amount', models.IntegerField(blank=True, null=True)),
                ('isAvailable', models.BooleanField(default=True)),
                ('isBillPaid', models.BooleanField(default=False)),
                ('Vehicle_license_plate', models.CharField(max_length=30)),
                ('customer_email', models.CharField(max_length=100)),
                ('request_responded_by', models.CharField(blank=True, max_length=100, null=True)),
                ('request_status', models.CharField(default='Pending', max_length=30)),
            ],
        ),
    ]