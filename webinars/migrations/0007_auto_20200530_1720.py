# Generated by Django 2.2 on 2020-05-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0006_auto_20200530_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webinar',
            name='image',
            field=models.ImageField(upload_to='webinars'),
        ),
    ]
