# Generated by Django 4.2.4 on 2023-09-26 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gramapanchayath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gramapanchayat1', models.CharField(max_length=255)),
                ('gramapanchayat2', models.CharField(max_length=255)),
                ('gramapanchayat3', models.CharField(max_length=255)),
                ('gramapanchayat4', models.CharField(max_length=255)),
                ('gramapanchayat5', models.CharField(max_length=255)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.staff')),
            ],
        ),
    ]
