# Generated by Django 2.1.5 on 2020-11-26 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0145_auto_20201126_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='t_information_item_tobeoperationalized_memor_timeseries',
            options={'ordering': ['action_datetime']},
        ),
        migrations.AlterModelOptions(
            name='t_information_item_tobeoperationalized_memor_timeseries_act',
            options={'ordering': ['action_description']},
        ),
    ]