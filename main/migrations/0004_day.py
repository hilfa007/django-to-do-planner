# Generated by Django 3.2.7 on 2022-07-08 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_todolistitems_checked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today', models.DateField(default=datetime.date(2022, 7, 8))),
            ],
        ),
    ]
