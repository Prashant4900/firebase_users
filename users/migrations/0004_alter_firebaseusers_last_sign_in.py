# Generated by Django 3.2.7 on 2021-09-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_firebaseusers_last_sign_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firebaseusers',
            name='last_sign_in',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
