# Generated by Django 2.1.2 on 2018-10-26 23:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0019_auto_20181021_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=True, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]