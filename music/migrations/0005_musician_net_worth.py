# Generated by Django 3.0.5 on 2020-04-19 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_album_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='net_worth',
            field=models.IntegerField(default=0),
        ),
    ]
