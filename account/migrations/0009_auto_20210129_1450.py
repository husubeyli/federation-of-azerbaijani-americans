# Generated by Django 3.1.5 on 2021-01-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210128_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationuser',
            name='membership_id',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Membership id'),
        ),
    ]