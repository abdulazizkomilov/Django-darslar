# Generated by Django 4.2.4 on 2023-09-13 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='info',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
