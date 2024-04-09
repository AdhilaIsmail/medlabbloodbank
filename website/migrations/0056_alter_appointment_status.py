# Generated by Django 4.2.4 on 2023-10-19 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0055_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(blank=True, choices=[('donated', 'Donated'), ('not_donated', 'Not Donated')], max_length=20, null=True),
        ),
    ]