# Generated by Django 3.2.7 on 2021-09-12 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_firebaseusers_last_sign_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firebaseusers',
            name='last_sign_in',
        ),
    ]
