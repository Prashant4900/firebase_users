# Generated by Django 3.2.7 on 2021-09-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DummyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Dummy',
            },
        ),
    ]