# Generated by Django 4.0.6 on 2022-08-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_studata_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='studata',
            name='center',
            field=models.TextField(default='', verbose_name='center'),
        ),
    ]
