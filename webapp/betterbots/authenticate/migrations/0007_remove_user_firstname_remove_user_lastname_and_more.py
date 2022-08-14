# Generated by Django 4.0.6 on 2022-08-11 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0006_user_city_user_country_user_firstname_user_lastname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.TextField(default='', max_length=30, verbose_name='full_name'),
        ),
    ]