# Generated by Django 3.2.7 on 2021-09-15 18:10

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210915_1613'),
        ('firestore', '0003_dummymodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummymodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.fields.CharField, to='users.firebaseusers'),
        ),
    ]
