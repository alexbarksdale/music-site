# Generated by Django 3.0.5 on 2020-04-19 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_musician_artist_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='artist_bio',
            field=models.CharField(default='', max_length=350),
        ),
    ]
