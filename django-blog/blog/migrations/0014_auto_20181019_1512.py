# Generated by Django 2.1.2 on 2018-10-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20181019_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=5000, null=True, verbose_name='İçerik'),
        ),
    ]