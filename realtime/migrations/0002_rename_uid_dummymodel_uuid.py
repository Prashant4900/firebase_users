# Generated by Django 3.2.7 on 2021-09-16 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtime', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dummymodel',
            old_name='uid',
            new_name='uuid',
        ),
    ]
