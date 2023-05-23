# Generated by Django 4.1.7 on 2023-05-15 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_appointment_name_alter_blog_poston'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='appointment',
            name='vehiclenumber',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='appointment',
            name='vehicleservices',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 5, 15)),
        ),
    ]
