# Generated by Django 3.2.6 on 2021-08-24 04:15

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('students', django.db.models.manager.Manager()),
            ],
        ),
    ]
