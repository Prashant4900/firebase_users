# Generated by Django 3.2.7 on 2021-09-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_firebaseusers_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firebaseusers',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='firebaseusers',
            name='provider',
            field=models.CharField(blank=True, default='Email', max_length=50),
        ),
    ]
