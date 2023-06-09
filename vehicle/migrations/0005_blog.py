# Generated by Django 4.1.7 on 2023-04-13 05:37

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_gallary'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField()),
                ('photo', models.ImageField(upload_to='blog/')),
                ('postby', models.CharField(default='Admin', max_length=50)),
                ('poston', models.DateField(default=datetime.date(2023, 4, 13))),
            ],
            options={
                'db_table': 'blogs',
            },
        ),
    ]
