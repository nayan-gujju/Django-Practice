# Generated by Django 3.2.6 on 2021-08-24 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_alter_page_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='user',
            field=models.OneToOneField(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
