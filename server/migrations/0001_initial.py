# Generated by Django 4.1.1 on 2022-09-14 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleName', models.CharField(max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('on', models.CharField(default='off', max_length=3)),
            ],
        ),
    ]
