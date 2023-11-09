# Generated by Django 4.2.4 on 2023-09-25 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('long', models.SmallIntegerField(default=0)),
                ('start', models.DateField()),
            ],
        ),
    ]
