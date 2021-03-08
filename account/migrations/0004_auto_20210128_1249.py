# Generated by Django 3.1.5 on 2021-01-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210128_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='memeber_of_ngo',
        ),
        migrations.AddField(
            model_name='user',
            name='member_of_ngo',
            field=models.CharField(default='', max_length=225, verbose_name='member of ngo'),
            preserve_default=False,
        ),
    ]
