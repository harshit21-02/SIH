# Generated by Django 4.0.6 on 2022-08-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0007_remove_user_firstname_remove_user_lastname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='centre',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pincode',
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.TextField(default='', verbose_name='gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='nationality',
            field=models.TextField(default='', verbose_name='ntly'),
        ),
        migrations.AddField(
            model_name='user',
            name='password1',
            field=models.TextField(default='', verbose_name='fpass'),
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.TextField(default='', verbose_name='spass'),
        ),
    ]
