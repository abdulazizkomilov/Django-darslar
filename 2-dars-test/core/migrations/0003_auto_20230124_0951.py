# Generated by Django 3.2.7 on 2023-01-24 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230124_0816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='post',
            name='sammury',
            field=models.CharField(default='ds', max_length=200),
            preserve_default=False,
        ),
    ]
