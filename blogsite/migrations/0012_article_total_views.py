# Generated by Django 2.2.3 on 2020-04-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0011_auto_20200331_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='total_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
