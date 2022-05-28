# Generated by Django 4.0.2 on 2022-05-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Manager_firstname', models.CharField(max_length=60)),
                ('Manager_lastname', models.CharField(max_length=60)),
                ('Manager_address', models.CharField(max_length=600)),
                ('Manager_email', models.CharField(max_length=100)),
                ('Manager_password', models.CharField(max_length=32)),
                ('Manager_dob', models.DateField()),
                ('Manager_mobileno', models.CharField(max_length=10)),
                ('Manager_gender', models.CharField(max_length=15)),
                ('Manager_license', models.ImageField(upload_to='img/Manager_License/')),
                ('Manager_agency', models.CharField(default='Fast Rentals', max_length=100)),
                ('Manager_city', models.CharField(max_length=30)),
                ('Manager_state', models.CharField(max_length=30)),
                ('Manager_country', models.CharField(max_length=30)),
                ('Manager_pincode', models.IntegerField()),
                ('isOwner', models.BooleanField(default=False)),
            ],
        ),
    ]
