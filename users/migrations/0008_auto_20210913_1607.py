# Generated by Django 3.2.7 on 2021-09-13 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_firebaseusers_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='firebaseusers',
            name='last_sign_in',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='firebaseusers',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
