# Generated by Django 5.0.2 on 2024-03-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0078_remove_labresult_booking_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
