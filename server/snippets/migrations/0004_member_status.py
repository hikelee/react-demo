# Generated by Django 2.0.1 on 2018-12-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_member_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '启用'), (2, '禁用')], default=1, verbose_name='状态'),
        ),
    ]
