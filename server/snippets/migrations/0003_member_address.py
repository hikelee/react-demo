# Generated by Django 2.0.1 on 2018-12-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20181219_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=500, null=True, verbose_name='地址'),
        ),
    ]
