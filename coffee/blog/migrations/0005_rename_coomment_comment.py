# Generated by Django 4.1.7 on 2023-04-10 10:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_coomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coomment',
            new_name='Comment',
        ),
    ]
