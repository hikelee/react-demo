# Generated by Django 2.0.1 on 2018-12-20 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_member_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birthday',
            field=models.DateField(null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='member',
            name='create_time',
            field=models.DateTimeField(null=True, verbose_name='加入时间'),
        ),
        migrations.AddField(
            model_name='member',
            name='signature',
            field=models.TextField(null=True, verbose_name='个性签名'),
        ),
        migrations.AddField(
            model_name='member',
            name='single',
            field=models.BooleanField(default=True, verbose_name='单身'),
        ),
    ]
