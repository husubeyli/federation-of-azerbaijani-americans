# Generated by Django 3.1.5 on 2021-02-08 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20210208_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donationuser',
            options={'ordering': ('-id',), 'verbose_name': 'Member', 'verbose_name_plural': 'Members'},
        ),
    ]