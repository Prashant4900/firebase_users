# Generated by Django 3.2.7 on 2021-09-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210913_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='firebaseusers',
            name='password',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]