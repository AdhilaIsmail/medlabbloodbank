# Generated by Django 4.2.4 on 2023-10-06 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_remove_hospitalregister_gpscoordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='lab_selection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.labselection'),
        ),
    ]
