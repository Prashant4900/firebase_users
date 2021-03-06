# Generated by Django 3.2.7 on 2021-09-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_firebaseusers_last_sign_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firebaseusers',
            name='create_at',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='firebaseusers',
            name='disabled',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='firebaseusers',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='firebaseusers',
            name='provider',
            field=models.CharField(blank=True, default='Email/Phone', max_length=50),
        ),
        migrations.AlterField(
            model_name='firebaseusers',
            name='user_image',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='firebaseusers',
            name='username',
            field=models.CharField(blank=True, default='Guest User', max_length=50),
        ),
        migrations.AlterField(
            model_name='firebaseusers',
            name='verified',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
