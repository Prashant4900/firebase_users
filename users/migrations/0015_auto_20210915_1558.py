# Generated by Django 3.2.7 on 2021-09-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210915_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firebaseusers',
            name='create_at',
            field=models.DateTimeField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='firebaseusers',
            name='last_sign_in',
            field=models.DateTimeField(blank=True, max_length=100),
        ),
    ]
