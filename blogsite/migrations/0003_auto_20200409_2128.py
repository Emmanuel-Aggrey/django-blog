# Generated by Django 2.2.3 on 2020-04-09 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0002_auto_20200409_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='author_writings', to=settings.AUTH_USER_MODEL),
        ),
    ]