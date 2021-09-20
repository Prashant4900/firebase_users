# Generated by Django 3.2.7 on 2021-09-16 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210915_1613'),
        ('realtime', '0002_rename_uid_dummymodel_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummymodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.firebaseusers'),
        ),
    ]